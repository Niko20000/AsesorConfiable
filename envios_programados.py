"""
envios_programados.py — Programar envíos automáticos por hora
Usa APScheduler para enviar mensajes en horarios específicos
"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import os
import json
from envio_masivo import EnvioMasivo

# Configuración
envio_masivo = EnvioMasivo(servidor_url=os.getenv("BOT_SERVER_URL", "http://localhost:3000"))
scheduler = BackgroundScheduler()

# Almacenar programaciones
programaciones = {}

def enviar_programado(id_programa, fuente, archivo, numeros_lista, mensaje):
    """Función que se ejecuta automáticamente a la hora programada"""
    print(f"\n{'='*60}")
    print(f"⏰ ENVIANDO PROGRAMACIÓN: {id_programa}")
    print(f"🕒 Hora: {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*60}\n")
    
    try:
        # Obtener números
        if fuente == "excel":
            numeros = envio_masivo.leer_excel(archivo)
        else:
            numeros = envio_masivo.leer_lista_texto(numeros_lista)
        
        if not numeros:
            print(f"❌ No se encontraron números para: {id_programa}")
            return
        
        # Enviar
        resultado = envio_masivo.enviar_masivo(numeros, mensaje, esperar_entre=True)
        
        # Guardar en log
        log_entrada = {
            "id": id_programa,
            "timestamp": datetime.now().isoformat(),
            "enviados": resultado['enviados'],
            "errores": resultado['errores'],
            "mensaje": mensaje[:100] + "..."
        }
        
        guardar_log(log_entrada)
        
        print(f"✅ Programación completada: {id_programa}")
        
    except Exception as e:
        print(f"❌ Error en programación {id_programa}: {e}")


def guardar_log(entrada):
    """Guardar en archivo de log"""
    try:
        with open("envios_log.json", "r", encoding="utf-8") as f:
            logs = json.load(f)
    except:
        logs = []
    
    logs.append(entrada)
    
    with open("envios_log.json", "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)


def programar_envio(id_programa, hora, minuto, fuente, archivo, numeros_lista, mensaje):
    """
    Programar envío a una hora específica (diariamente)
    
    Ejemplo:
    programar_envio(
        "envio_mañana",
        hora=8,           # 8:00 AM
        minuto=0,
        fuente="excel",
        archivo="numeros.xlsx",
        numeros_lista=None,
        mensaje="¡Buen día!"
    )
    """
    
    # Validar
    if not (0 <= hora <= 23):
        return {"error": "Hora debe estar entre 0 y 23"}
    if not (0 <= minuto <= 59):
        return {"error": "Minuto debe estar entre 0 y 59"}
    
    # Crear trigger CRON (diariamente a esa hora)
    trigger = CronTrigger(hour=hora, minute=minuto)
    
    # Agregar job al scheduler
    job = scheduler.add_job(
        enviar_programado,
        trigger=trigger,
        args=[id_programa, fuente, archivo, numeros_lista, mensaje],
        id=id_programa,
        name=f"Envío {id_programa} - {hora:02d}:{minuto:02d}",
        replace_existing=True
    )
    
    # Guardar en memoria
    programaciones[id_programa] = {
        "hora": hora,
        "minuto": minuto,
        "fuente": fuente,
        "archivo": archivo,
        "numeros": numeros_lista,
        "mensaje": mensaje[:100] + "...",
        "proxima_ejecucion": job.next_run_time.isoformat() if job.next_run_time else None,
        "activo": True
    }
    
    print(f"✅ Envío programado: {id_programa} a las {hora:02d}:{minuto:02d} diariamente")
    
    return {
        "success": True,
        "id": id_programa,
        "hora": f"{hora:02d}:{minuto:02d}",
        "proxima_ejecucion": str(job.next_run_time)
    }


def cancelar_programacion(id_programa):
    """Cancelar una programación existente"""
    try:
        scheduler.remove_job(id_programa)
        programaciones[id_programa]["activo"] = False
        print(f"❌ Programación cancelada: {id_programa}")
        return {"success": True, "message": f"Programación {id_programa} cancelada"}
    except Exception as e:
        return {"error": str(e)}


def obtener_programaciones():
    """Obtener lista de todas las programaciones"""
    return programaciones


def obtener_historial():
    """Obtener historial de envíos programados"""
    try:
        with open("envios_log.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def iniciar_scheduler():
    """Iniciar el scheduler"""
    if not scheduler.running:
        scheduler.start()
        print("✅ Scheduler de envíos programados iniciado")


def detener_scheduler():
    """Detener el scheduler"""
    if scheduler.running:
        scheduler.shutdown()
        print("❌ Scheduler detenido")


# ─────────────────────────────────────────────
# EJEMPLOS DE USO
# ─────────────────────────────────────────────

if __name__ == "__main__":
    
    # Iniciar scheduler
    iniciar_scheduler()
    
    # EJEMPLO 1: Programar envío diario a las 8:00 AM
    programar_envio(
        id_programa="buenos_dias",
        hora=8,
        minuto=0,
        fuente="excel",
        archivo="numeros.xlsx",
        numeros_lista=None,
        mensaje="☀️ ¡Buenos días! Bienvenido a Banco Caja Social 😊\n\n¿En qué puedo ayudarte hoy?"
    )
    
    # EJEMPLO 2: Programar envío a las 2:00 PM
    programar_envio(
        id_programa="oferta_tarde",
        hora=14,
        minuto=0,
        fuente="excel",
        archivo="numeros.xlsx",
        numeros_lista=None,
        mensaje="🎁 ¡Oferta especial de la tarde!\n\nCréditos con tasas especiales solo hoy. ¿Te interesa?"
    )
    
    # EJEMPLO 3: Programar con números manuales a las 6:00 PM
    programar_envio(
        id_programa="recordatorio_cierre",
        hora=18,
        minuto=0,
        fuente="lista",
        archivo=None,
        numeros_lista=["573001234567", "573005678901"],
        mensaje="👋 Antes de cerremos... ¿Completamos tu solicitud? ¡Es rápido! 😊"
    )
    
    # Ver programaciones
    print("\n📋 PROGRAMACIONES ACTIVAS:")
    for id_prog, datos in obtener_programaciones().items():
        print(f"  • {id_prog}: {datos['hora']}:{datos['minuto']:02d} - {datos['proxima_ejecucion']}")
    
    # Ver historial
    print("\n📊 HISTORIAL DE ENVÍOS:")
    historial = obtener_historial()
    for entrada in historial[-5:]:
        print(f"  • {entrada['timestamp']}: {entrada['id']} - Enviados: {entrada['enviados']}")
    
    # Mantener scheduler corriendo
    try:
        import time
        print("\n✅ Scheduler en ejecución. Presiona Ctrl+C para detener.\n")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        detener_scheduler()
        print("\n👋 Scheduler detenido")