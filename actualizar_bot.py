"""
actualizar_bot.py — Script para agregar cambios a bot.py de forma segura
Ejecutar: python actualizar_bot.py
"""

import os
import re
from pathlib import Path

# Colores para terminal
class Color:
    VERDE = '\033[92m'
    ROJO = '\033[91m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    FIN = '\033[0m'

def crear_backup(archivo):
    """Crear backup del archivo original"""
    if os.path.exists(archivo):
        backup = f"{archivo}.backup"
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        with open(backup, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"{Color.VERDE}✅ Backup creado: {backup}{Color.FIN}")
        return True
    return False

def agregar_imports_bot(contenido_bot):
    """Agregar imports necesarios al bot.py"""
    
    # Verificar si ya existen
    if "from envio_masivo import EnvioMasivo" in contenido_bot:
        print(f"{Color.AMARILLO}⚠️  Imports de envío masivo ya existen{Color.FIN}")
        return contenido_bot
    
    if "from envios_programados import" in contenido_bot:
        print(f"{Color.AMARILLO}⚠️  Imports de envíos programados ya existen{Color.FIN}")
        return contenido_bot
    
    # Encontrar donde insertar (después de otros imports)
    lineas = contenido_bot.split('\n')
    
    # Buscar la última línea de import
    ultimo_import = 0
    for i, linea in enumerate(lineas):
        if linea.startswith('from ') or linea.startswith('import '):
            ultimo_import = i
    
    # Insertar nuevos imports después del último
    nuevos_imports = '\n# ─────────────────────────────────────────────\n# ENVÍO MASIVO Y PROGRAMADO\n# ─────────────────────────────────────────────\n\ntry:\n    from envio_masivo import EnvioMasivo\n    from envios_programados import (\n        programar_envio, cancelar_programacion,\n        obtener_programaciones, obtener_historial,\n        iniciar_scheduler\n    )\n    ENVIO_MASIVO_DISPONIBLE = True\nexcept ImportError:\n    print("⚠️  Módulos de envío no disponibles. Instala: pip install apscheduler")\n    ENVIO_MASIVO_DISPONIBLE = False\n'
    
    lineas.insert(ultimo_import + 1, nuevos_imports)
    
    return '\n'.join(lineas)

def agregar_endpoints(contenido_bot):
    """Agregar endpoints sin tocar código existente"""
    
    # Verificar si ya existen
    if "/envio-masivo" in contenido_bot:
        print(f"{Color.AMARILLO}⚠️  Endpoints de envío ya existen{Color.FIN}")
        return contenido_bot
    
    # Endpoints a agregar
    endpoints = '''

# ─────────────────────────────────────────────
# ENVÍO MASIVO — Endpoints
# ─────────────────────────────────────────────

if ENVIO_MASIVO_DISPONIBLE:
    envio_masivo = EnvioMasivo(servidor_url=os.getenv("BOT_SERVER_URL", "http://localhost:3000"))

    @app.route("/envio-masivo", methods=["POST"])
    def envio_masivo_endpoint():
        """
        Endpoint para enviar mensajes masivos.
        
        POST /envio-masivo
        {
            "fuente": "excel" | "lista",
            "archivo": "numeros.xlsx",
            "numeros": ["573001234567", "573005678901"],
            "mensaje": "Tu mensaje aquí",
            "clave_admin": "tu_clave"
        }
        """
        data = request.json
        clave = data.get("clave_admin")
        
        # Verificar contraseña
        CLAVE_ADMIN = os.getenv("CLAVE_ENVIO_MASIVO", "cambiar_esto_por_segura")
        
        if clave != CLAVE_ADMIN:
            return jsonify({"error": "Clave de administrador incorrecta"}), 403
        
        fuente = data.get("fuente", "lista")
        mensaje = data.get("mensaje", "")
        
        if not mensaje:
            return jsonify({"error": "El mensaje es requerido"}), 400
        
        try:
            # Obtener números
            if fuente == "excel":
                archivo = data.get("archivo", "numeros.xlsx")
                numeros = envio_masivo.leer_excel(archivo)
            elif fuente == "lista":
                numeros_lista = data.get("numeros", [])
                numeros = envio_masivo.leer_lista_texto(numeros_lista)
            else:
                return jsonify({"error": "Fuente debe ser 'excel' o 'lista'"}), 400
            
            if not numeros:
                return jsonify({"error": "No se encontraron números"}), 400
            
            # Enviar mensajes
            resultado = envio_masivo.enviar_masivo(numeros, mensaje, esperar_entre=True)
            
            return jsonify({
                "success": True,
                "resumen": resultado,
                "timestamp": datetime.now().isoformat()
            })
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/envio-masivo/status", methods=["GET"])
    def envio_masivo_status():
        """Ver estado de los últimos envíos masivos"""
        return jsonify({
            "enviados": len(envio_masivo.enviados),
            "errores": len(envio_masivo.errores),
            "ultimos_envios": envio_masivo.enviados[-10:] if envio_masivo.enviados else [],
            "ultimos_errores": envio_masivo.errores[-10:] if envio_masivo.errores else []
        })

# ─────────────────────────────────────────────
# ENVÍOS PROGRAMADOS — Endpoints
# ─────────────────────────────────────────────

if ENVIO_MASIVO_DISPONIBLE:
    # Iniciar scheduler al arrancar
    iniciar_scheduler()

    @app.route("/programar-envio", methods=["POST"])
    def programar_envio_endpoint():
        """
        Programar envío automático a una hora específica
        
        POST /programar-envio
        {
            "clave_admin": "tu_clave",
            "id_programa": "buenos_dias",
            "hora": 8,
            "minuto": 0,
            "fuente": "excel",
            "archivo": "numeros.xlsx",
            "mensaje": "¡Buenos días!"
        }
        """
        data = request.json
        clave = data.get("clave_admin")
        
        # Verificar contraseña
        CLAVE_ADMIN = os.getenv("CLAVE_ENVIO_MASIVO", "cambiar_esto_por_segura")
        
        if clave != CLAVE_ADMIN:
            return jsonify({"error": "Clave de administrador incorrecta"}), 403
        
        try:
            resultado = programar_envio(
                id_programa=data.get("id_programa"),
                hora=int(data.get("hora", 8)),
                minuto=int(data.get("minuto", 0)),
                fuente=data.get("fuente", "excel"),
                archivo=data.get("archivo", "numeros.xlsx"),
                numeros_lista=data.get("numeros_lista"),
                mensaje=data.get("mensaje", "")
            )
            
            return jsonify(resultado)
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/cancelar-envio/<id_programa>", methods=["POST"])
    def cancelar_envio_endpoint(id_programa):
        """Cancelar una programación existente"""
        data = request.json
        clave = data.get("clave_admin")
        
        CLAVE_ADMIN = os.getenv("CLAVE_ENVIO_MASIVO", "cambiar_esto_por_segura")
        
        if clave != CLAVE_ADMIN:
            return jsonify({"error": "Clave de administrador incorrecta"}), 403
        
        resultado = cancelar_programacion(id_programa)
        return jsonify(resultado)

    @app.route("/programaciones", methods=["GET"])
    def obtener_programaciones_endpoint():
        """Ver todas las programaciones activas"""
        return jsonify({
            "programaciones": obtener_programaciones(),
            "total": len(obtener_programaciones())
        })

    @app.route("/historial-envios", methods=["GET"])
    def historial_envios_endpoint():
        """Ver historial de envíos programados"""
        return jsonify({
            "historial": obtener_historial(),
            "total": len(obtener_historial())
        })
'''
    
    # Insertar antes de "if __name__"
    if 'if __name__ == "__main__"' in contenido_bot:
        contenido_bot = contenido_bot.replace(
            'if __name__ == "__main__"',
            endpoints + '\n\nif __name__ == "__main__"'
        )
        print(f"{Color.VERDE}✅ Endpoints agregados correctamente{Color.FIN}")
        return contenido_bot
    else:
        print(f"{Color.ROJO}❌ No se encontró 'if __name__' en bot.py{Color.FIN}")
        return contenido_bot

def actualizar_env():
    """Actualizar o crear archivo .env"""
    archivo_env = ".env"
    
    clave_necesaria = "CLAVE_ENVIO_MASIVO"
    
    if os.path.exists(archivo_env):
        with open(archivo_env, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        if clave_necesaria not in contenido:
            with open(archivo_env, 'a', encoding='utf-8') as f:
                f.write(f"\n{clave_necesaria}=Alex123456\n")
            print(f"{Color.VERDE}✅ Clave agregada a .env{Color.FIN}")
        else:
            print(f"{Color.AMARILLO}⚠️  {clave_necesaria} ya existe en .env{Color.FIN}")
    else:
        with open(archivo_env, 'w', encoding='utf-8') as f:
            f.write(f"""ANTHROPIC_API_KEY=tu_clave_aqui
BOT_SERVER_URL=http://localhost:3000
NUMERO_ASESOR=573505494401
{clave_necesaria}=Alex123456
""")
        print(f"{Color.VERDE}✅ Archivo .env creado{Color.FIN}")

def verificar_archivos():
    """Verificar que existan todos los archivos necesarios"""
    archivos_necesarios = [
        'envio_masivo.py',
        'envios_programados.py',
        'bot.py',
        'mensajes.py',
        'whatsapp-bridge.js'
    ]
    
    print(f"\n{Color.AZUL}📋 Verificando archivos necesarios:{Color.FIN}")
    faltantes = []
    
    for archivo in archivos_necesarios:
        if os.path.exists(archivo):
            tamaño = os.path.getsize(archivo) / 1024  # KB
            print(f"{Color.VERDE}✅ {archivo}{Color.FIN} ({tamaño:.1f} KB)")
        else:
            print(f"{Color.ROJO}❌ {archivo}{Color.FIN}")
            if archivo not in ['whatsapp-bridge.js']:  # whatsapp-bridge es Node.js
                faltantes.append(archivo)
    
    return len(faltantes) == 0

def main():
    print(f"\n{Color.AZUL}{'='*60}{Color.FIN}")
    print(f"{Color.AZUL}🤖 ACTUALIZAR BOT.PY CON ENVÍO MASIVO{Color.FIN}")
    print(f"{Color.AZUL}{'='*60}{Color.FIN}\n")
    
    # Verificar archivos
    if not verificar_archivos():
        print(f"\n{Color.ROJO}⚠️  Faltan archivos. Asegúrate de tener todos los archivos necesarios.{Color.FIN}")
        return False
    
    # Crear backup
    print(f"\n{Color.AZUL}📦 Creando backup...{Color.FIN}")
    crear_backup("bot.py")
    
    # Leer bot.py actual
    print(f"\n{Color.AZUL}📖 Leyendo bot.py actual...{Color.FIN}")
    with open("bot.py", 'r', encoding='utf-8') as f:
        contenido_bot = f.read()
    
    lineas_originales = len(contenido_bot.split('\n'))
    print(f"   Líneas actuales: {lineas_originales}")
    
    # Agregar imports
    print(f"\n{Color.AZUL}➕ Agregando imports...{Color.FIN}")
    contenido_bot = agregar_imports_bot(contenido_bot)
    
    # Agregar endpoints
    print(f"\n{Color.AZUL}➕ Agregando endpoints...{Color.FIN}")
    contenido_bot = agregar_endpoints(contenido_bot)
    
    # Guardar bot.py actualizado
    print(f"\n{Color.AZUL}💾 Guardando bot.py actualizado...{Color.FIN}")
    with open("bot.py", 'w', encoding='utf-8') as f:
        f.write(contenido_bot)
    
    lineas_nuevas = len(contenido_bot.split('\n'))
    print(f"   Líneas originales: {lineas_originales}")
    print(f"   Líneas nuevas: {lineas_nuevas}")
    print(f"   {Color.VERDE}✅ Líneas agregadas: {lineas_nuevas - lineas_originales}{Color.FIN}")
    
    # Actualizar .env
    print(f"\n{Color.AZUL}⚙️  Actualizando .env...{Color.FIN}")
    actualizar_env()
    
    # Resumen final
    print(f"\n{Color.VERDE}{'='*60}{Color.FIN}")
    print(f"{Color.VERDE}✅ ¡ACTUALIZACIÓN COMPLETADA!{Color.FIN}")
    print(f"{Color.VERDE}{'='*60}{Color.FIN}\n")
    
    print(f"{Color.AZUL}📋 Próximos pasos:{Color.FIN}")
    print(f"   1. Instala apscheduler: {Color.AMARILLO}pip install apscheduler{Color.FIN}")
    print(f"   2. Ejecuta el bot: {Color.AMARILLO}python bot.py{Color.FIN}")
    print(f"   3. Abre el panel web: {Color.AMARILLO}admin_envios_mejorado.html{Color.FIN}")
    
    print(f"\n{Color.AZUL}📁 Archivos creados/modificados:{Color.FIN}")
    print(f"   • {Color.VERDE}bot.py{Color.FIN} (actualizado)")
    print(f"   • {Color.VERDE}.env{Color.FIN} (actualizado)")
    print(f"   • {Color.VERDE}envio_masivo.py{Color.FIN} (debe existir)")
    print(f"   • {Color.VERDE}envios_programados.py{Color.FIN} (debe existir)")
    print(f"   • {Color.VERDE}admin_envios_mejorado.html{Color.FIN} (debe existir)")
    
    print(f"\n{Color.AMARILLO}💡 Si algo falla, tu backup está en: bot.py.backup{Color.FIN}\n")
    
    return True

if __name__ == "__main__":
    main()