"""
test_envio.py - Script para probar envío masivo
Ejecutar: python test_envio.py
"""

import requests
import json

# URL de la API
API_URL = "http://localhost:5000"

# Tus números
numeros = [
    "573505494401",  # Tu número de prueba
]

# Mensaje
mensaje = "¡Hola! Prueba del bot de envío masivo 🚀"

# Tu clave
clave = "Alex123456"

# Enviar
print("🚀 Enviando mensaje masivo...")
print(f"Números: {numeros}")
print(f"Mensaje: {mensaje}")
print(f"URL: {API_URL}/envio-masivo\n")

try:
    response = requests.post(
        f"{API_URL}/envio-masivo",
        json={
            "fuente": "lista",
            "numeros": numeros,
            "mensaje": mensaje,
            "clave_admin": clave
        }
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Respuesta:")
    print(json.dumps(response.json(), indent=2))
    
    if response.status_code == 200:
        print("\n✅ ¡ÉXITO! El envío masivo funciona")
    else:
        print(f"\n❌ Error: {response.json().get('error')}")
        
except requests.exceptions.ConnectionError:
    print("❌ ERROR DE CONEXIÓN")
    print("No se puede conectar a http://localhost:5000")
    print("Verifica que Python esté corriendo: python bot.py")
except Exception as e:
    print(f"❌ Error: {e}")