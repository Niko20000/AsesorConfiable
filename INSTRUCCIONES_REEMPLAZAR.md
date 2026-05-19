# 📥 INSTRUCCIONES PARA REEMPLAZAR ARCHIVOS

## ✅ RESUMEN DE LO QUE HE HECHO

He corregido todos los errores de tu `bot.py`:

1. ✅ **Arreglé los imports** - El try/except estaba en medio de los imports de mensajes
2. ✅ **Definí `ENVIO_MASIVO_DISPONIBLE`** correctamente
3. ✅ **Agregué todos los endpoints** sin borrar tu código original
4. ✅ **bot.py sigue con 1110 líneas** (tu código se preservó)
5. ✅ **Sin errores de compilación**

---

## 📂 ARCHIVOS A DESCARGAR Y REEMPLAZAR

Descarga estos 7 archivos:

| Archivo | Acción |
|---------|--------|
| `bot.py` | ✅ REEMPLAZAR el antiguo |
| `.env` | ✅ REEMPLAZAR o CREAR |
| `envio_masivo.py` | ✅ VERIFICAR que exista |
| `envios_programados.py` | ✅ VERIFICAR que exista |
| `admin_envios_mejorado.html` | ✅ REEMPLAZAR o CREAR |
| `requirements.txt` | ✅ REEMPLAZAR |
| `README_ACTUALIZADO.md` | ℹ️ Información |

---

## 🚀 PASOS DE INSTALACIÓN

### PASO 1: Descargar los Archivos

Descarga estos 7 archivos de los outputs:
- `bot.py`
- `.env`
- `envio_masivo.py`
- `envios_programados.py`
- `admin_envios_mejorado.html`
- `requirements.txt`
- `README_ACTUALIZADO.md`

### PASO 2: Reemplazar en tu Carpeta

Tu carpeta debe verse así:

```
tu-bot/
├── bot.py                       ← Reemplazado ✅
├── mensajes.py                  ← (sin cambios)
├── envio_masivo.py              ← Descargado ✅
├── envios_programados.py        ← Descargado ✅
├── admin_envios_mejorado.html   ← Descargado ✅
├── whatsapp-bridge.js           ← (sin cambios)
├── package.json                 ← (sin cambios)
├── .env                         ← Actualizado ✅
└── requirements.txt             ← Actualizado ✅
```

### PASO 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Si ya las tienes, ejecuta:

```bash
pip install -r requirements.txt --upgrade
```

### PASO 4: Configurar .env

Abre el archivo `.env` y actualiza con tus valores:

```env
ANTHROPIC_API_KEY=sk-ant-tu-clave-aqui
BOT_SERVER_URL=http://localhost:3000
NUMERO_ASESOR=573505494401
CLAVE_ENVIO_MASIVO=Alex123456
```

**Importante:** Cambia `sk-ant-tu-clave-aqui` por tu clave real de Claude API

### PASO 5: Verificar que Funciona

En terminal:

```bash
python -m py_compile bot.py
```

Si no hay error, está bien. Ahora:

```bash
python bot.py
```

**Deberías ver:**

```
✅ Módulos de envío masivo cargados correctamente
✅ Scheduler de envíos programados iniciado
✅ Base de datos lista
🏦 Banco Caja Social — Alex Martínez
🧠 IA activa | 🚀 http://localhost:5000
```

### PASO 6: Iniciar Node.js (otra terminal)

```bash
npm install
node whatsapp-bridge.js
```

### PASO 7: Usar el Panel Web

Abre en navegador: `admin_envios_mejorado.html`

Usa la clave que pusiste en `.env` (por defecto: `Alex123456`)

---

## ✨ NUEVAS FUNCIONALIDADES

Tu bot ahora tiene:

### 🚀 Envío Masivo Inmediato
- Envía mensajes a múltiples números ahora
- Desde panel web o API
- Respeta límites de WhatsApp

### ⏰ Envíos Programados
- Programa un mensaje para una hora específica
- Se envía automáticamente cada día a esa hora
- Ejemplo: Enviar "Buenos días" a las 8:00 AM

### 📋 Mis Programaciones
- Ver todas las programaciones activas
- Cancelar programaciones que no quieras
- Ver cuándo se ejecutarán

### 📊 Historial
- Ver todos los envíos realizados
- Cuántos se enviaron exitosamente
- Cuántos tuvieron errores

---

## 🔍 VERIFICACIÓN RÁPIDA

Después de instalar, verifica:

```bash
# Ver cuántas líneas tiene el bot
wc -l bot.py
# Debería salir algo como: 1110 bot.py

# Buscar los endpoints nuevos
grep -c "envio-masivo" bot.py
grep -c "programar-envio" bot.py
# Ambos deberían salir ≥ 1

# Compilar sin errores
python -m py_compile bot.py
# No debería mostrar error
```

---

## 📞 SI ALGO FALLA

### Error: "Módulos de envío no disponibles"
```bash
pip install apscheduler openpyxl
```

### Error: "No se encuentra bot.py"
Asegúrate de ejecutar el comando desde la carpeta del bot:
```bash
cd /ruta/a/tu/carpeta/del/bot
python bot.py
```

### Error: "CLAVE_ENVIO_MASIVO no encontrada"
Verifica que `.env` esté en la misma carpeta que `bot.py`

### Error: "Clave incorrecta en panel web"
La clave debe coincidir exactamente con la de `.env`
(por defecto es `Alex123456`)

---

## 📋 CHECKLIST FINAL

Antes de decir que terminaste:

- ☑️ Descargué los 7 archivos
- ☑️ Reemplacé `bot.py` en mi carpeta
- ☑️ Reemplacé `.env` y actualicé mi clave de API
- ☑️ Reemplacé `requirements.txt`
- ☑️ Instalé dependencias: `pip install -r requirements.txt`
- ☑️ Ejecuté: `python bot.py` y veo mensajes de éxito
- ☑️ Ejecuté: `node whatsapp-bridge.js` en otra terminal
- ☑️ Abrí el panel web en navegador
- ☑️ Probé enviar un mensaje masivo
- ☑️ Probé programar un envío para una hora

---

## ✅ ¡LISTO!

Una vez completado el checklist, tu bot estará:

✨ **Funcionando sin errores**  
🚀 **Con envío masivo inmediato**  
⏰ **Con envíos programados automáticos**  
📊 **Con historial y estadísticas**  
🔐 **Protegido con clave de administrador**

---

**¡Dime cuando lo hayas hecho y verificamos que funcione! 🎉**
