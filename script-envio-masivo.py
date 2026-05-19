#!/usr/bin/env python3
"""
script_envio_masivo.py — Envía mensajes masivos de forma interactiva
Ejecutar: python script_envio_masivo.py
"""

from envio_masivo import EnvioMasivo
import sys

def mostrar_menu():
    print("\n" + "="*60)
    print("📱 ENVÍO MASIVO — BANCO CAJA SOCIAL")
    print("="*60)
    print("\n¿De dónde quieres cargar los números?\n")
    print("1️⃣  Desde archivo Excel (numeros.xlsx)")
    print("2️⃣  Desde lista manual (escribir números)")
    print("3️⃣  Ver estado de últimos envíos")
    print("0️⃣  Salir\n")
    
    return input("Elige una opción (0-3): ").strip()

def opcion_excel():
    envio = EnvioMasivo()
    archivo = input("\n📁 Nombre del archivo (default: numeros.xlsx): ").strip() or "numeros.xlsx"
    
    numeros = envio.leer_excel(archivo)
    if not numeros:
        return
    
    print(f"\n📋 Se encontraron {len(numeros)} números:")
    for i, dato in enumerate(numeros[:5], 1):
        print(f"   {i}. {dato['nombre']} ({dato['numero']}) - Grupo: {dato['grupo']}")
    if len(numeros) > 5:
        print(f"   ... y {len(numeros)-5} más")
    
    confirmar = input(f"\n¿Enviar a todos estos {len(numeros)} números? (s/n): ").lower()
    if confirmar != 's':
        print("❌ Cancelado")
        return
    
    print("\n📝 Escribe el mensaje a enviar (presiona Enter dos veces para terminar):")
    lineas = []
    while True:
        linea = input()
        if linea == "":
            if lineas and lineas[-1] == "":
                lineas.pop()
                break
            lineas.append("")
        else:
            lineas.append(linea)
    
    mensaje = "\n".join(lineas)
    
    if not mensaje.strip():
        print("❌ El mensaje no puede estar vacío")
        return
    
    resultado = envio.enviar_masivo(numeros, mensaje, esperar_entre=True)
    
    print("\n✅ RESUMEN:")
    print(f"   Enviados: {resultado['enviados']}")
    print(f"   Errores: {resultado['errores']}")

def opcion_lista():
    envio = EnvioMasivo()
    
    print("\n📱 Ingresa los números (uno por línea, sin + ni espacios)")
    print("Ejemplo: 573001234567")
    print("Presiona Enter dos veces para terminar:\n")
    
    numeros_input = []
    while True:
        num = input()
        if num == "":
            if numeros_input and numeros_input[-1] == "":
                numeros_input.pop()
                break
            numeros_input.append("")
        else:
            numeros_input.append(num)
    
    numeros_input = [n for n in numeros_input if n.strip()]
    
    if not numeros_input:
        print("❌ No ingresaste números")
        return
    
    numeros = envio.leer_lista_texto(numeros_input)
    
    print(f"\n✅ Se cargaron {len(numeros)} números")
    confirmar = input("¿Continuar? (s/n): ").lower()
    if confirmar != 's':
        return
    
    print("\n📝 Escribe el mensaje a enviar:\n")
    lineas = []
    while True:
        linea = input()
        if linea == "":
            if lineas and lineas[-1] == "":
                lineas.pop()
                break
            lineas.append("")
        else:
            lineas.append(linea)
    
    mensaje = "\n".join(lineas)
    
    if not mensaje.strip():
        print("❌ El mensaje no puede estar vacío")
        return
    
    resultado = envio.enviar_masivo(numeros, mensaje, esperar_entre=True)
    
    print("\n✅ RESUMEN:")
    print(f"   Enviados: {resultado['enviados']}")
    print(f"   Errores: {resultado['errores']}")

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            opcion_excel()
        elif opcion == "2":
            opcion_lista()
        elif opcion == "3":
            print("\n📊 Estado (implementar según necesidad)")
        elif opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    main()