# 🤖 Bot WhatsApp Financiera

Bot de WhatsApp con IA para atender clientes de créditos personales, préstamos rápidos y compra de cartera.

---

## ¿Qué hace este bot?

- ✅ Responde preguntas generales con IA (Claude / Sofía)
- ✅ Guía al cliente paso a paso para solicitar un crédito
- ✅ Captura: nombre, cédula, ingresos, actividad, antigüedad, monto, correo
- ✅ Guarda todo en SQLite (local) y Supabase (nube)
- ✅ Te notifica a tu número real cuando llega una solicitud nueva

---

## INSTALACIÓN PASO A PASO

### Requisitos previos
- Python 3.10 o superior
- Node.js 18 o superior
- Una tarjeta SIM nueva con número para el bot

---

### PASO 1 — Clonar y preparar archivos

```bash
# Entra a la carpeta del proyecto
cd whatsapp-bot

# Copia el archivo de configuración
cp .env.example .env
```

Abre `.env` y llena:
- `ANTHROPIC_API_KEY` → consíguelo en https://console.anthropic.com
- `MI_NUMERO_REAL` → tu número personal (ej: 573001234567)
- `SUPABASE_URL` y `SUPABASE_KEY` → de tu proyecto en https://supabase.com

---

### PASO 2 — Configurar Supabase (nube)

1. Entra a https://supabase.com y crea una cuenta gratis
2. Crea un nuevo proyecto
3. Ve a **SQL Editor** y pega el contenido de `supabase_setup.sql`
4. Ejecuta el script (botón Run)
5. Ve a **Settings → API** y copia la URL y la `anon key` a tu `.env`

---

### PASO 3 — Instalar dependencias Python

```bash
pip install -r requirements.txt
```

---

### PASO 4 — Instalar dependencias Node.js

```bash
npm install
```

---

### PASO 5 — Iniciar el bot

Necesitas **dos terminales abiertas**:

**Terminal 1 — Bot Python (la inteligencia)**
```bash
python bot.py
```
Verás: `🚀 Servidor Python corriendo en http://localhost:5000`

**Terminal 2 — Puente WhatsApp (la conexión)**
```bash
node whatsapp-bridge.js
```
Verás un QR en la terminal. **Escanéalo con el número nuevo** desde WhatsApp → ⋮ → Dispositivos vinculados.

---

### PASO 6 — Probar

Envía un mensaje al número nuevo desde cualquier WhatsApp:
```
Hola, ¿qué servicios tienen?
```

El bot debe responder automáticamente. 🎉

---

## FLUJO DE CONVERSACIÓN

```
Cliente: "Hola"
   ↓
Sofía (IA): Saluda y explica los servicios

Cliente: "Quiero un préstamo"
   ↓
Sofía: Inicia el formulario paso a paso
  1. Nombre completo
  2. Cédula
  3. Ingresos mensuales
  4. Actividad / ocupación
  5. Antigüedad laboral
  6. Monto solicitado
  7. Correo electrónico
   ↓
Bot: Guarda en SQLite + Supabase
Bot: Te envía notificación a tu WhatsApp real
Bot: Le dice al cliente que lo contactarán
```

---

## VER SOLICITUDES GUARDADAS

**SQLite (local):**
```bash
sqlite3 clientes.db "SELECT nombre, monto, fecha FROM solicitudes ORDER BY fecha DESC;"
```

**API local:**
```
GET http://localhost:5000/solicitudes
```

**Supabase (desde el celular):**
Entra a tu proyecto en https://supabase.com → Table Editor → solicitudes

---

## PERSONALIZAR EL BOT

Para cambiar la personalidad o información del bot, edita el `SISTEMA_PROMPT` en `bot.py`:

```python
SISTEMA_PROMPT = """Eres un asesor virtual de créditos...
[Aquí puedes agregar tasas, requisitos, horarios, etc.]
"""
```

---

## MANTENERLO ENCENDIDO (Producción)

Para que el bot no se apague cuando cierres la terminal:

```bash
# Instalar PM2
npm install -g pm2

# Iniciar el puente Node.js
pm2 start whatsapp-bridge.js --name "whatsapp-bridge"

# Iniciar el bot Python
pm2 start bot.py --interpreter python3 --name "bot-python"

# Ver estado
pm2 status

# Ver logs en vivo
pm2 logs
```

---

## ESTRUCTURA DEL PROYECTO

```
whatsapp-bot/
├── bot.py                # Lógica del bot (Python + IA)
├── whatsapp-bridge.js    # Conexión WhatsApp (Node.js)
├── requirements.txt      # Dependencias Python
├── package.json          # Dependencias Node.js
├── supabase_setup.sql    # Script para crear tabla en Supabase
├── .env.example          # Plantilla de configuración
├── .env                  # Tu configuración (NO subir a Git)
└── clientes.db           # Base de datos local (se crea automático)
```

---

## ⚠️ IMPORTANTE

- Este bot usa `whatsapp-web.js` que **no es oficial de WhatsApp**. Úsalo responsablemente.
- No uses el número del bot para spam — solo para atender clientes que te escriban.
- Haz backup de `clientes.db` periódicamente.
- Supabase gratis tiene límite de 500MB — suficiente para miles de solicitudes.
