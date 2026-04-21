"""
bot.py — Banco Caja Social / Alex Martínez

Cambios aplicados:
1. Filtro de groserías — nunca se toman como nombre ni se repiten
2. Startup delay fix — reintento si Python no está listo
3. Simulación universal — créditos, seguros y ahorro. Sin total_pagado/intereses
4. Formulario para TODOS los servicios
5. Fix "5 millones" — orden correcto en parsear_monto
6. Calidez mantenida
7. Manejo de audios — respuesta amable
"""

import os
import re
import sqlite3
import requests
from datetime import datetime
from anthropic import Anthropic
from flask import Flask, request, jsonify
from dotenv import load_dotenv

from mensajes import (
    NOMBRE_ASESOR, BANCO, NUMERO_ASESOR, SISTEMA_PROMPT,
    TASAS_MV, MAPA_SERVICIO_TASA,
    SEGUROS_DETALLE, PDF_SEGUROS, SEGUROS_PLANES,
    MSG_LISTA_PDFS, MSG_OFERTA_PDFS_POST_SOLICITUD, MSG_OFERTA_PDFS_PROACTIVA,
    MSG_BIENVENIDA_NOMBRE,
    MSG_PRE_SIM_MONTO, MSG_PRE_SIM_MESES, MSG_PRE_SIM_RESULTADO,
    MSG_SIM_SEGURO, MSG_SIM_AHORRO,
    MSG_SIM_NO_APLICA, MSG_CONFIRMAR_APLICAR,
    SIMULADOR_MENU, MSG_SIMULADOR_MONTO, MSG_SIMULADOR_MESES,
    MSG_RESULTADO_SIMULACION, MSG_MESES_INVALIDOS,
    MSG_SIMULADOR_PROD_INVALIDO,
    MSG_PEDIR_NOMBRE, MSG_RETRY_NOMBRE,
    MSG_PEDIR_CEDULA, MSG_RETRY_CEDULA,
    MSG_PEDIR_INGRESOS, MSG_RETRY_INGRESOS,
    MSG_PEDIR_ACTIVIDAD, MSG_RETRY_ACTIVIDAD,
    MSG_PEDIR_ANTIGUEDAD, MSG_CONFIRMAR_ANTIGUEDAD,
    MSG_PEDIR_CORREO, MSG_RETRY_CORREO,
    MSG_PEDIR_CELULAR, MSG_RETRY_CELULAR,
    MSG_RESUMEN, MSG_CORREGIR_DATOS,
    MSG_CIERRE_CALIDO, MSG_RECIBO_FINAL, MSG_RESUMEN_ASESOR,
    MSG_ERROR_TECNICO, MSG_AUDIO_NO_SOPORTADO,
    MSG_RESPUESTA_GROSER, PALABRAS_GROSERAS,
)

load_dotenv()

app    = Flask(__name__)
claude = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# ─────────────────────────────────────────────
# ESTADO EN MEMORIA
# ─────────────────────────────────────────────

estados_memoria = {}

def get_estado(telefono):
    return estados_memoria.get(telefono, {"etapa": "inicio", "datos": {}})

def set_estado(telefono, etapa, datos):
    estados_memoria[telefono] = {"etapa": etapa, "datos": datos}

# ─────────────────────────────────────────────
# HISTORIAL
# ─────────────────────────────────────────────

def init_db():
    conn = sqlite3.connect("conversaciones.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS conversaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telefono TEXT, rol TEXT, mensaje TEXT, fecha TEXT
    )""")
    conn.commit()
    conn.close()

def guardar_mensaje(telefono, rol, mensaje):
    conn = sqlite3.connect("conversaciones.db")
    c = conn.cursor()
    c.execute("INSERT INTO conversaciones (telefono, rol, mensaje, fecha) VALUES (?,?,?,?)",
              (telefono, rol, mensaje, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def obtener_historial(telefono, limite=14):
    conn = sqlite3.connect("conversaciones.db")
    c = conn.cursor()
    c.execute("SELECT rol, mensaje FROM conversaciones WHERE telefono=? ORDER BY fecha DESC LIMIT ?",
              (telefono, limite))
    rows = c.fetchall()
    conn.close()
    return [{"role": r[0], "content": r[1]} for r in reversed(rows)]

# ─────────────────────────────────────────────
# NOTIFICACIONES
# ─────────────────────────────────────────────

def notificar_asesor(mensaje):
    servidor = os.getenv("BOT_SERVER_URL", "http://localhost:3000")
    try:
        requests.post(f"{servidor}/send", json={"phone": NUMERO_ASESOR, "message": mensaje}, timeout=5)
        print("📲 Asesor notificado")
    except Exception as e:
        print(f"❌ Notificación fallida: {e}")

def notificar_error(telefono_cliente, error):
    num = telefono_cliente.replace("@lid","").replace("@c.us","").replace("@s.whatsapp.net","")
    notificar_asesor(
        f"*⚠️ PROBLEMA TÉCNICO*\nCliente: +{num}\n"
        f"Hora: {datetime.now().strftime('%d/%m/%Y %H:%M')}\nError: {error[:200]}"
    )

# ─────────────────────────────────────────────
# VALIDACIONES
# ─────────────────────────────────────────────

NO_ES_NOMBRE = {
    "si","sí","no","su","ok","yes","nel","dale","hola","gracias","listo","claro",
    "bien","perfecto","correcto","omitir","nada","nunca","siempre","todo","algo",
    "dame","quiero","necesito","haber","ver","saber","tengo","tiene","tenemos",
    "un","una","el","la","los","las","de","del","al","por","para","con","sin",
}

PALABRAS_NO_NOMBRE = {
    "quiero","necesito","dame","busco","tengo","tiene","tenemos","quiere",
    "saber","ver","poder","hacer","ir","venir","hablar","llamar","contactar",
    "credito","crédito","prestamo","préstamo","vivienda","libranza","cartera",
    "simulacion","simulación","seguro","ahorro","inversion","inversión",
    "pdf","lista","documento","información","informacion","ayuda","folleto",
    "el","la","los","las","un","una","de","del","al","por","para","con","sin",
    "que","y","o","es","son","hay","puede","a","e","ni","pero","mas","más",
    "banco","caja","social","asesor","agente","persona","señor","señora",
    "libre","compra","mejoramiento","hipotecario",
}

CONFIRMACIONES = {"si","sí","yes","s","correcto","ok","claro","todo bien",
                  "esta bien","está bien","adelante","dale","listo","exacto"}
NEGACIONES     = {"no","nel","nope","no gracias","no quiero","en otro momento",
                  "despues","después","luego","ahora no"}

def contiene_groseria(texto):
    """True si el texto contiene alguna grosería."""
    t = texto.lower().strip()
    palabras = re.findall(r'\w+', t)
    for p in palabras:
        if p in PALABRAS_GROSERAS:
            return True
    return False

def parece_nombre(texto):
    t = texto.strip().lower()
    palabras = t.split()
    if len(palabras) > 4 or len(t) < 2 or len(t) > 50:
        return False
    if t in NO_ES_NOMBRE:
        return False
    # Rechazar groserías como nombres
    if contiene_groseria(t):
        return False
    for p in palabras:
        if p in PALABRAS_NO_NOMBRE:
            return False
    alpha = sum(1 for c in t if c.isalpha() or c == ' ')
    return alpha >= len(t) * 0.85

def parece_cedula(texto):
    t = re.sub(r'[\s\.\-]', '', texto.strip())
    if len(t) < 5 or len(t) > 15:
        return False
    return sum(c.isdigit() for c in t) >= len(t) * 0.7

def parece_monto_ingreso(texto):
    t = texto.lower().strip()
    return bool(re.search(r'\d', t)) or any(k in t for k in ["mil","millon","millón","smmlv"])

def parece_correo(texto):
    return bool(re.match(r'.+@.+\..+', texto.strip()))

def parece_celular(texto):
    t = re.sub(r'[\s\+\-\(\)]', '', texto.strip())
    return len(t) >= 7 and sum(c.isdigit() for c in t) >= len(t) * 0.8

def parece_actividad(texto):
    t = texto.strip().lower()
    if len(t) < 3:
        return False
    if t in CONFIRMACIONES or t in NEGACIONES:
        return False
    return True

# ─────────────────────────────────────────────
# UTILIDADES — CAMBIO 5: Fix "5 millones"
# ─────────────────────────────────────────────

def parsear_monto(texto):
    """
    Convierte texto a (formato, número).
    FIX: reemplaza 'millones' ANTES de 'millon' para evitar bug de parseo.
    Ejemplos: '5 millones' → $5.000.000, '500 mil' → $500.000
    """
    t = texto.lower().strip()
    try:
        # IMPORTANTE: plurales primero, luego singulares
        t = t.replace("millones", "000000").replace("millónes", "000000")
        t = t.replace("millon",   "000000").replace("millón",   "000000")
        t = t.replace("mil", "000")
        t = t.replace("pesos","").replace("cop","").replace("smmlv","")
        t = t.replace("$","").replace(".","").replace(",","").replace(" ","").strip()
        num = int(float(t))
        if num <= 0:
            return texto, None
        return f"${num:,}".replace(",","."), num
    except:
        return texto, None

def parsear_meses(texto):
    try:
        t = texto.lower().strip()
        if "año" in t:
            num = float(re.search(r'[\d.]+', t).group())
            return int(num * 12)
        return int(float(re.search(r'[\d]+', t).group()))
    except:
        return None

def obtener_tasa(servicio):
    clave = MAPA_SERVICIO_TASA.get(servicio, "1")
    return TASAS_MV[clave]

def _extraer_nombre_historial(historial):
    for msg in historial:
        if msg.get("role") == "user":
            c = msg.get("content","").strip()
            palabras = c.split()
            if 1 <= len(palabras) <= 4 and parece_nombre(c):
                return c
    return ""

# ─────────────────────────────────────────────
# LÓGICA PRINCIPAL
# ─────────────────────────────────────────────

def procesar_mensaje(telefono, texto, imagen_info=None, es_audio=False):
    # CAMBIO 7: Manejo de audios
    if es_audio:
        guardar_mensaje(telefono, "user", "[AUDIO]")
        guardar_mensaje(telefono, "assistant", MSG_AUDIO_NO_SOPORTADO)
        return {"reply": MSG_AUDIO_NO_SOPORTADO}

    estado = get_estado(telefono)
    etapa  = estado["etapa"]
    datos  = estado["datos"]
    extra  = {}

    guardar_mensaje(telefono, "user", texto)
    tl = texto.lower().strip()

    # CAMBIO 1: Filtro de groserías — responde con calma, no repite la grosería
    if contiene_groseria(tl):
        guardar_mensaje(telefono, "assistant", MSG_RESPUESTA_GROSER)
        return {"reply": MSG_RESPUESTA_GROSER}

    # ── Detectar petición de PDFs fuera del formulario ──
    etapas_formulario = {
        "pre_sim_monto","pre_sim_meses","pre_sim_confirmar",
        "pre_sim_seguro_confirmar","pre_sim_ahorro_monto","pre_sim_ahorro_dias",
        "pre_sim_ahorro_confirmar",
        "sim_eligiendo_producto","sim_pidiendo_monto","sim_pidiendo_meses",
        "preguntando_nombre","preguntando_cedula","preguntando_ingresos",
        "preguntando_actividad","preguntando_antiguedad","confirmando_antiguedad",
        "preguntando_monto_form","preguntando_correo","preguntando_celular",
        "confirmando_resumen",
    }
    palabras_pdf = ["pdf","documento","folleto","brochure","catalogo","catálogo",
                    "lista","archivos","materiales"]
    if any(p in tl for p in palabras_pdf) and etapa not in etapas_formulario:
        guardar_mensaje(telefono, "assistant", MSG_LISTA_PDFS)
        return {"reply": MSG_LISTA_PDFS}

    # ══════════════════════════════════════════
    # SIMULACIÓN PREVIA — CRÉDITOS
    # ══════════════════════════════════════════

    if etapa == "pre_sim_monto":
        texto_fmt, num = parsear_monto(texto)
        if num and num > 0:
            datos["monto"]     = texto_fmt
            datos["monto_num"] = num
            set_estado(telefono, "pre_sim_meses", datos)
            respuesta = MSG_PRE_SIM_MESES
        else:
            respuesta = "No pude entender el monto. 😊\n\nEscríbelo así: 5 millones, 500 mil, 2.000.000..."

    elif etapa == "pre_sim_meses":
        meses = parsear_meses(texto)
        if meses and 10 <= meses <= 240:
            tasa_info = obtener_tasa(datos.get("servicio","libre_inversion"))
            respuesta = MSG_PRE_SIM_RESULTADO(
                tasa_info["nombre"], datos["monto_num"], meses,
                tasa_info["tasa_mv"], tasa_info["desde_ea"], tasa_info["hasta_ea"]
            )
            datos["meses_sim"] = meses
            set_estado(telefono, "pre_sim_confirmar", datos)
        else:
            respuesta = MSG_MESES_INVALIDOS

    elif etapa == "pre_sim_confirmar":
        if tl in NEGACIONES:
            set_estado(telefono, "inicio", {})
            respuesta = MSG_SIM_NO_APLICA
        elif tl in CONFIRMACIONES:
            nombre_guardado = datos.get("nombre","")
            if nombre_guardado and parece_nombre(nombre_guardado):
                set_estado(telefono, "preguntando_cedula", datos)
                respuesta = MSG_PEDIR_CEDULA(nombre_guardado.split()[0])
            else:
                set_estado(telefono, "preguntando_nombre", datos)
                respuesta = "¡Perfecto! Empecemos. 😊\n\n" + MSG_PEDIR_NOMBRE
        else:
            respuesta = MSG_CONFIRMAR_APLICAR

    # ══════════════════════════════════════════
    # SIMULACIÓN PREVIA — SEGUROS (CAMBIO 3)
    # ══════════════════════════════════════════

    elif etapa == "pre_sim_seguro_confirmar":
        if tl in NEGACIONES:
            set_estado(telefono, "inicio", {})
            respuesta = MSG_SIM_NO_APLICA
        elif tl in CONFIRMACIONES:
            nombre_guardado = datos.get("nombre","")
            if nombre_guardado and parece_nombre(nombre_guardado):
                set_estado(telefono, "preguntando_cedula", datos)
                respuesta = MSG_PEDIR_CEDULA(nombre_guardado.split()[0])
            else:
                set_estado(telefono, "preguntando_nombre", datos)
                respuesta = "¡Perfecto! Empecemos. 😊\n\n" + MSG_PEDIR_NOMBRE
        else:
            respuesta = MSG_CONFIRMAR_APLICAR

    # ══════════════════════════════════════════
    # SIMULACIÓN PREVIA — AHORRO (CAMBIO 3)
    # ══════════════════════════════════════════

    elif etapa == "pre_sim_ahorro_monto":
        texto_fmt, num = parsear_monto(texto)
        if num and num > 0:
            datos["monto"]     = texto_fmt
            datos["monto_num"] = num
            set_estado(telefono, "pre_sim_ahorro_dias", datos)
            respuesta = (
                "¿A cuántos días te gustaría invertirlo? 📅\n\n"
                "Ejemplo: 60, 90, 180, 360 días..."
            )
        else:
            respuesta = "No pude entender el monto. 😊\n\nEscríbelo así: 5 millones, 500 mil, 2.000.000..."

    elif etapa == "pre_sim_ahorro_dias":
        try:
            dias = int(re.search(r'\d+', texto).group())
            if 30 <= dias <= 540:
                respuesta = MSG_SIM_AHORRO(datos["monto_num"], dias)
                datos["dias_sim"] = dias
                set_estado(telefono, "pre_sim_ahorro_confirmar", datos)
            else:
                respuesta = "Por favor escribe un número entre *30 y 540* días. 😊\nEjemplo: 60, 90, 180, 360..."
        except:
            respuesta = "Por favor escribe el número de días. 😊\nEjemplo: 60, 90, 180, 360..."

    elif etapa == "pre_sim_ahorro_confirmar":
        if tl in NEGACIONES:
            set_estado(telefono, "inicio", {})
            respuesta = MSG_SIM_NO_APLICA
        elif tl in CONFIRMACIONES:
            nombre_guardado = datos.get("nombre","")
            if nombre_guardado and parece_nombre(nombre_guardado):
                set_estado(telefono, "preguntando_cedula", datos)
                respuesta = MSG_PEDIR_CEDULA(nombre_guardado.split()[0])
            else:
                set_estado(telefono, "preguntando_nombre", datos)
                respuesta = "¡Perfecto! Empecemos. 😊\n\n" + MSG_PEDIR_NOMBRE
        else:
            respuesta = MSG_CONFIRMAR_APLICAR

    # ══════════════════════════════════════════
    # SIMULADOR INDEPENDIENTE
    # ══════════════════════════════════════════

    elif etapa == "sim_eligiendo_producto":
        if tl in TASAS_MV:
            datos["sim_producto_key"]    = tl
            datos["sim_producto_nombre"] = TASAS_MV[tl]["nombre"]
            set_estado(telefono, "sim_pidiendo_monto", datos)
            respuesta = MSG_SIMULADOR_MONTO
        else:
            respuesta = MSG_SIMULADOR_PROD_INVALIDO

    elif etapa == "sim_pidiendo_monto":
        texto_fmt, num = parsear_monto(texto)
        if num and num > 0:
            datos["sim_monto_fmt"] = texto_fmt
            datos["sim_monto_num"] = num
            set_estado(telefono, "sim_pidiendo_meses", datos)
            respuesta = MSG_SIMULADOR_MESES
        else:
            respuesta = "No pude entender el monto. 😊\n\nEscríbelo así: 5 millones, 500 mil..."

    elif etapa == "sim_pidiendo_meses":
        meses = parsear_meses(texto)
        if meses and 10 <= meses <= 240:
            key  = datos["sim_producto_key"]
            info = TASAS_MV[key]
            respuesta = MSG_RESULTADO_SIMULACION(
                info["nombre"], datos["sim_monto_num"], meses,
                info["tasa_mv"], info["desde_ea"], info["hasta_ea"]
            )
            set_estado(telefono, "inicio", {})
        else:
            respuesta = MSG_MESES_INVALIDOS

    # ══════════════════════════════════════════
    # FORMULARIO CON VALIDACIÓN — CAMBIO 4: aplica para todos los servicios
    # ══════════════════════════════════════════

    elif etapa == "preguntando_nombre":
        if parece_nombre(texto):
            datos["nombre"] = texto
            set_estado(telefono, "preguntando_cedula", datos)
            respuesta = MSG_PEDIR_CEDULA(texto.split()[0])
        else:
            respuesta = MSG_RETRY_NOMBRE

    elif etapa == "preguntando_cedula":
        if parece_cedula(texto):
            datos["cedula"] = texto
            set_estado(telefono, "preguntando_ingresos", datos)
            respuesta = MSG_PEDIR_INGRESOS
        else:
            respuesta = MSG_RETRY_CEDULA

    elif etapa == "preguntando_ingresos":
        if parece_monto_ingreso(texto):
            datos["ingresos"] = texto
            set_estado(telefono, "preguntando_actividad", datos)
            respuesta = MSG_PEDIR_ACTIVIDAD
        else:
            respuesta = MSG_RETRY_INGRESOS

    elif etapa == "preguntando_actividad":
        if parece_actividad(texto):
            datos["actividad"] = texto
            set_estado(telefono, "preguntando_antiguedad", datos)
            respuesta = MSG_PEDIR_ANTIGUEDAD
        else:
            respuesta = MSG_RETRY_ACTIVIDAD

    elif etapa == "preguntando_antiguedad":
        datos["antiguedad_pendiente"] = texto
        set_estado(telefono, "confirmando_antiguedad", datos)
        respuesta = MSG_CONFIRMAR_ANTIGUEDAD(texto)

    elif etapa == "confirmando_antiguedad":
        datos["antiguedad"] = datos.get("antiguedad_pendiente", texto) if tl in CONFIRMACIONES else texto
        if datos.get("monto"):
            set_estado(telefono, "preguntando_correo", datos)
            respuesta = MSG_PEDIR_CORREO
        else:
            set_estado(telefono, "preguntando_monto_form", datos)
            respuesta = "¿Cuál es el *monto* o *plan* que te interesa? 💰\n\nEjemplo: 2 millones, 500 mil, o el plan del seguro..."

    elif etapa == "preguntando_monto_form":
        if len(texto.strip()) >= 2:
            texto_fmt, num = parsear_monto(texto)
            datos["monto"] = texto_fmt if num else texto
            set_estado(telefono, "preguntando_correo", datos)
            respuesta = MSG_PEDIR_CORREO
        else:
            respuesta = "Por favor escribe el monto o plan que te interesa. 😊"

    elif etapa == "preguntando_correo":
        if parece_correo(texto):
            datos["correo"] = texto
            set_estado(telefono, "preguntando_celular", datos)
            respuesta = MSG_PEDIR_CELULAR
        else:
            respuesta = MSG_RETRY_CORREO

    elif etapa == "preguntando_celular":
        if parece_celular(texto):
            datos["celular"] = texto
            set_estado(telefono, "confirmando_resumen", datos)
            respuesta = MSG_RESUMEN(datos)
        else:
            respuesta = MSG_RETRY_CELULAR

    elif etapa == "confirmando_resumen":
        if tl in CONFIRMACIONES:
            datos["telefono"] = telefono
            d = datos
            numero_limpio = telefono.replace("@lid","").replace("@c.us","").replace("@s.whatsapp.net","")
            nombre_corto  = d.get("nombre","").split()[0] if d.get("nombre") else ""

            msg_cierre     = MSG_CIERRE_CALIDO(nombre_corto)
            msg_recibo     = MSG_RECIBO_FINAL(d)
            resumen_asesor = MSG_RESUMEN_ASESOR(d, numero_limpio)

            notificar_asesor(resumen_asesor)
            set_estado(telefono, "post_solicitud", {})
            guardar_mensaje(telefono, "assistant", msg_cierre)
            guardar_mensaje(telefono, "assistant", msg_recibo)
            return {
                "reply": msg_cierre,
                "reply2": msg_recibo,
                "notificar_asesor": True,
                "numero_asesor": NUMERO_ASESOR,
                "mensaje_asesor": resumen_asesor,
            }
        else:
            set_estado(telefono, "inicio", datos)
            respuesta = MSG_CORREGIR_DATOS

    elif etapa == "post_solicitud":
        if tl in NEGACIONES or tl in {"omitir","no","nel","no gracias"}:
            set_estado(telefono, "inicio", {})
            respuesta = "¡Perfecto! Cuando necesites algo más, aquí estaré. 😊\n\nQue tengas un excelente día."
        elif tl in SEGUROS_DETALLE:
            respuesta = SEGUROS_DETALLE[tl]
            pdf_info  = PDF_SEGUROS.get(tl)
            if pdf_info:
                extra["enviar_pdf"]  = pdf_info["archivo"]
                extra["caption_pdf"] = pdf_info["caption"]
            set_estado(telefono, "inicio", {})
        else:
            set_estado(telefono, "inicio", {})
            respuesta = MSG_OFERTA_PDFS_POST_SOLICITUD

    # ══════════════════════════════════════════
    # CONVERSACIÓN LIBRE CON IA
    # ══════════════════════════════════════════

    else:
        historial = obtener_historial(telefono)
        historial.append({"role": "user", "content": texto})
        historial_limpio = [
            m for m in historial
            if m.get("content","").strip() and m["content"] not in ["[IMAGEN_RECIBIDA]","[AUDIO]"]
        ] or [{"role": "user", "content": texto}]

        try:
            resp_ia = claude.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=450,
                system=SISTEMA_PROMPT,
                messages=historial_limpio
            )
            respuesta = resp_ia.content[0].text.strip()
        except Exception as e:
            print(f"❌ Error IA: {e}")
            notificar_error(telefono, str(e))
            respuesta = MSG_ERROR_TECNICO

        # ── [INICIAR_CREDITO:tipo] ──
        match_credito = re.search(r'\[INICIAR_CREDITO:(\w+)\]', respuesta)
        # ── [INICIAR_SEGURO:numero] ──
        match_seguro = re.search(r'\[INICIAR_SEGURO:(\w+)\]', respuesta)
        # ── [INICIAR_AHORRO] ──
        match_ahorro = "[INICIAR_AHORRO]" in respuesta

        if match_credito:
            tipo = match_credito.group(1)
            respuesta_limpia = re.sub(r'\[INICIAR_CREDITO:\w+\]', '', respuesta).strip()
            nombre_en_conv   = _extraer_nombre_historial(historial)
            datos_nuevos     = {"servicio": tipo, "nombre": nombre_en_conv}
            # Nombre del servicio para el resumen
            tasa_info = obtener_tasa(tipo)
            datos_nuevos["servicio_nombre"] = tasa_info["nombre"]
            set_estado(telefono, "pre_sim_monto", datos_nuevos)
            nombre_msg = nombre_en_conv.split()[0] if nombre_en_conv else ""
            respuesta  = (respuesta_limpia + "\n\n" + MSG_PRE_SIM_MONTO(nombre_msg)).strip()

        elif match_seguro:
            num_seguro = match_seguro.group(1)
            respuesta_limpia = re.sub(r'\[INICIAR_SEGURO:\w+\]', '', respuesta).strip()
            nombre_en_conv   = _extraer_nombre_historial(historial)
            plan_info        = SEGUROS_PLANES.get(num_seguro, {})
            datos_nuevos = {
                "servicio": f"seguro_{num_seguro}",
                "servicio_nombre": plan_info.get("nombre", f"Seguro {num_seguro}"),
                "nombre": nombre_en_conv,
            }
            set_estado(telefono, "pre_sim_seguro_confirmar", datos_nuevos)
            sim_msg = MSG_SIM_SEGURO(
                plan_info.get("nombre", f"Seguro {num_seguro}"),
                plan_info.get("desde", "según plan"),
                plan_info.get("hasta", "según plan")
            )
            respuesta = (respuesta_limpia + "\n\n" + sim_msg).strip()

        elif match_ahorro:
            respuesta_limpia = re.sub(r'\[INICIAR_AHORRO\]', '', respuesta).strip()
            nombre_en_conv   = _extraer_nombre_historial(historial)
            datos_nuevos = {
                "servicio": "ahorro_inversion",
                "servicio_nombre": "Ahorro e Inversión",
                "nombre": nombre_en_conv,
            }
            set_estado(telefono, "pre_sim_ahorro_monto", datos_nuevos)
            nombre_msg = nombre_en_conv.split()[0] if nombre_en_conv else ""
            intro = f"Con mucho gusto, *{nombre_msg}*. 😊\n\n" if nombre_msg else "Con mucho gusto. 😊\n\n"
            respuesta = (
                respuesta_limpia + "\n\n" + intro +
                "Para mostrarte un ejemplo real de rendimiento, "
                "¿cuánto dinero te gustaría invertir?\n\n"
                "Puedes escribirlo como quieras: 5 millones, 500 mil, 2.000.000..."
            ).strip()

        elif "[INICIAR_SIMULADOR]" in respuesta:
            respuesta_limpia = re.sub(r'\[INICIAR_SIMULADOR\]', '', respuesta).strip()
            set_estado(telefono, "sim_eligiendo_producto", {})
            respuesta = (respuesta_limpia + "\n\n" + SIMULADOR_MENU).strip()

        elif "[MOSTRAR_PDFS]" in respuesta:
            respuesta = MSG_LISTA_PDFS
            set_estado(telefono, "inicio", datos)

        elif tl in SEGUROS_DETALLE:
            respuesta = SEGUROS_DETALLE[tl]
            pdf_info  = PDF_SEGUROS.get(tl)
            if pdf_info:
                extra["enviar_pdf"]  = pdf_info["archivo"]
                extra["caption_pdf"] = pdf_info["caption"]
            extra["reply2"] = MSG_OFERTA_PDFS_PROACTIVA
            set_estado(telefono, "inicio", datos)

        else:
            set_estado(telefono, "inicio", datos)

    guardar_mensaje(telefono, "assistant", respuesta)
    return {"reply": respuesta, **extra}


# ─────────────────────────────────────────────
# ENDPOINTS
# ─────────────────────────────────────────────

@app.route("/mensaje", methods=["POST"])
def recibir_mensaje():
    data      = request.json
    telefono  = data.get("from")
    texto     = data.get("body","")
    imagen    = data.get("imagen")
    es_audio  = data.get("es_audio", False)  # CAMBIO 7

    if not telefono:
        return jsonify({"error": "Datos incompletos"}), 400

    print(f"📩 [{telefono}]: {texto}")
    resultado = procesar_mensaje(telefono, texto, imagen, es_audio)
    print(f"🤖 {NOMBRE_ASESOR}: {resultado.get('reply','')[:80]}")
    return jsonify(resultado)


@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "activo",
        "asesor": NOMBRE_ASESOR,
        "banco": BANCO,
        "clientes_en_sesion": len(estados_memoria)
    })


if __name__ == "__main__":
    init_db()
    print(f"✅ Base de datos lista")
    print(f"🏦 {BANCO} — {NOMBRE_ASESOR}")
    print(f"🧠 IA activa | 🚀 http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)