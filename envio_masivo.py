"""
envio_masivo.py — Funciones para enviar mensajes a múltiples números
Lee desde Excel o lista de números
"""

import openpyxl
import requests
import time
from datetime import datetime

class EnvioMasivo:
    def __init__(self, servidor_url="http://localhost:3000"):
        self.servidor = servidor_url
        self.enviados = []
        self.errores = []
    
    def leer_excel(self, archivo="numeros.xlsx"):
        """Lee números del archivo Excel y retorna lista de dicts."""
        try:
            wb = openpyxl.load_workbook(archivo)
            ws = wb.active
            
            numeros = []
            for row in ws.iter_rows(min_row=2, values_only=True):  # Saltar encabezado
                if row[0]:  # Si hay número
                    numero = str(row[0]).strip()
                    # Limpiar formato
                    numero = numero.replace("+", "").replace(" ", "")
                    
                    nombre = str(row[1]).strip() if len(row) > 1 and row[1] else "Usuario"
                    grupo = str(row[2]).strip() if len(row) > 2 and row[2] else "General"
                    
                    numeros.append({
                        "numero": numero,
                        "nombre": nombre,
                        "grupo": grupo
                    })
            
            print(f"✅ Se leyeron {len(numeros)} números del Excel")
            return numeros
        
        except FileNotFoundError:
            print(f"❌ Archivo {archivo} no encontrado")
            return []
        except Exception as e:
            print(f"❌ Error al leer Excel: {e}")
            return []
    
    def leer_lista_texto(self, numeros_lista):
        """
        Convierte una lista de números en formato de dict.
        Acepta: ["57300123456", "57300654321"] o con +
        """
        numeros = []
        for num in numeros_lista:
            num_limpio = str(num).strip().replace("+", "").replace(" ", "")
            numeros.append({
                "numero": num_limpio,
                "nombre": "Usuario",
                "grupo": "General"
            })
        return numeros
    
    def enviar_mensaje(self, numero, mensaje, esperar=False):
        """
        Envía un mensaje a un número específico vía WhatsApp Bridge
        """
        try:
            payload = {
                "phone": numero,
                "message": mensaje
            }
            response = requests.post(
                f"{self.servidor}/send",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                self.enviados.append({
                    "numero": numero,
                    "timestamp": datetime.now().isoformat(),
                    "status": "exitoso"
                })
                print(f"✅ Enviado a: +{numero}")
                if esperar:
                    time.sleep(1)  # Esperar 1 segundo entre mensajes
                return True
            else:
                self.errores.append({
                    "numero": numero,
                    "error": response.text,
                    "timestamp": datetime.now().isoformat()
                })
                print(f"❌ Error al enviar a +{numero}: {response.status_code}")
                return False
        
        except Exception as e:
            self.errores.append({
                "numero": numero,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            })
            print(f"❌ Excepción enviando a +{numero}: {e}")
            return False
    
    def enviar_masivo(self, numeros, mensaje, esperar_entre=True):
        """
        Envía el mismo mensaje a múltiples números.
        Si esperar_entre=True, espera 1 segundo entre cada envío para evitar bloqueos.
        """
        print(f"\n🚀 Iniciando envío masivo a {len(numeros)} números...")
        print(f"📱 Mensaje: {mensaje[:50]}...\n")
        
        for idx, dato in enumerate(numeros, 1):
            numero = dato["numero"]
            nombre = dato.get("nombre", "Usuario")
            
            print(f"[{idx}/{len(numeros)}] Enviando a {nombre} (+{numero})...")
            self.enviar_mensaje(numero, mensaje, esperar=esperar_entre)
        
        self._mostrar_resumen()
        return {
            "enviados": len(self.enviados),
            "errores": len(self.errores),
            "detalles_enviados": self.enviados,
            "detalles_errores": self.errores
        }
    
    def enviar_con_personalizacion(self, numeros, plantilla_mensaje):
        """
        Envía mensajes personalizados usando una plantilla.
        plantilla_mensaje debe ser una función que reciba el dict del usuario.
        
        Ejemplo:
        def mi_plantilla(usuario):
            return f"¡Hola {usuario['nombre']}! Bienvenido al grupo {usuario['grupo']}"
        
        envio.enviar_con_personalizacion(numeros, mi_plantilla)
        """
        print(f"\n🚀 Enviando mensajes personalizados a {len(numeros)} números...\n")
        
        for idx, dato in enumerate(numeros, 1):
            numero = dato["numero"]
            nombre = dato.get("nombre", "Usuario")
            
            # Generar mensaje personalizado
            mensaje = plantilla_mensaje(dato)
            
            print(f"[{idx}/{len(numeros)}] Enviando a {nombre}...")
            self.enviar_mensaje(numero, mensaje, esperar=True)
        
        self._mostrar_resumen()
        return {
            "enviados": len(self.enviados),
            "errores": len(self.errores),
        }
    
    def _mostrar_resumen(self):
        """Muestra resumen de envíos"""
        total = len(self.enviados) + len(self.errores)
        print(f"\n{'='*50}")
        print(f"📊 RESUMEN DE ENVÍO")
        print(f"{'='*50}")
        print(f"✅ Enviados: {len(self.enviados)}/{total}")
        print(f"❌ Errores:  {len(self.errores)}/{total}")
        print(f"{'='*50}\n")


# ─────────────────────────────────────────────
# EJEMPLOS DE USO
# ─────────────────────────────────────────────

if __name__ == "__main__":
    envio = EnvioMasivo()
    
    # OPCIÓN 1: Leer desde Excel
    print("\n📋 OPCIÓN 1: Desde Excel")
    numeros = envio.leer_excel("numeros.xlsx")
    
    mensaje = "¡Hola! 👋 Soy Alex Martínez del Banco Caja Social. ¿Cómo estás? 😊"
    resultado = envio.enviar_masivo(numeros, mensaje, esperar_entre=True)
    
    # OPCIÓN 2: Lista directa en Python
    print("\n📱 OPCIÓN 2: Lista en Python")
    numeros_lista = [
        "573001234567",
        "573005678901",
        "573009876543"
    ]
    numeros = envio.leer_lista_texto(numeros_lista)
    resultado = envio.enviar_masivo(numeros, mensaje, esperar_entre=True)
    
    # OPCIÓN 3: Mensajes personalizados
    print("\n✨ OPCIÓN 3: Mensajes Personalizados")
    
    def plantilla_personalizada(usuario):
        return f"""¡Hola {usuario['nombre']}! 👋

Soy *Alex Martínez*, Ejecutivo Comercial del *Banco Caja Social*.

Vi que eres del grupo *{usuario['grupo']}* y te quería ofrecerte nuestros mejores productos:

✅ Créditos con tasas preferenciales
✅ Seguros protegidos
✅ Ahorro e inversión

¿Te gustaría saber más? 😊

Escribe *1* para info | *2* para dejar tus datos"""
    
    resultado = envio.enviar_con_personalizacion(numeros, plantilla_personalizada)