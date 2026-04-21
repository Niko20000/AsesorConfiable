/**
 * Puente WhatsApp → Python
 * - Manejo de audios (CAMBIO 7)
 * - Retry al startup si Python no está listo (CAMBIO 2)
 * - Envío de PDFs automático
 */

const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const axios  = require('axios');
const express = require('express');
const fs   = require('fs');
const path = require('path');

const app = express();
app.use(express.json({ limit: '50mb' }));

const PYTHON_BOT_URL = 'http://127.0.0.1:5000/mensaje';
const PDFS_DIR = path.join(__dirname, 'pdfs');

if (!fs.existsSync(PDFS_DIR)) {
    fs.mkdirSync(PDFS_DIR, { recursive: true });
}

const client = new Client({
    authStrategy: new LocalAuth({ clientId: "financiera-bot" }),
    puppeteer: {
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    }
});

client.on('qr', (qr) => {
    console.log('\n📱 Escanea este QR con tu WhatsApp nuevo:\n');
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('✅ WhatsApp conectado y listo!');
    const archivos = fs.existsSync(PDFS_DIR)
        ? fs.readdirSync(PDFS_DIR).filter(f => f.endsWith('.pdf'))
        : [];
    if (archivos.length > 0) {
        console.log(`📄 PDFs cargados: ${archivos.join(', ')}`);
    } else {
        console.log('⚠️  No hay PDFs en la carpeta /pdfs/ todavía.');
    }
    console.log('🤖 Bot activo — esperando mensajes...\n');
});

client.on('auth_failure', () => {
    console.error('❌ Error de autenticación. Borra .wwebjs_auth y vuelve a escanear.');
});

client.on('disconnected', (reason) => {
    console.log('⚠️  WhatsApp desconectado:', reason);
});

// ── Enviar PDF al cliente ──
async function enviarPDF(chatId, nombreArchivo, caption) {
    try {
        const rutaPDF = path.join(PDFS_DIR, nombreArchivo);
        if (!fs.existsSync(rutaPDF)) {
            console.log(`⚠️  PDF no encontrado: ${nombreArchivo}`);
            return false;
        }
        const media = MessageMedia.fromFilePath(rutaPDF);
        await client.sendMessage(chatId, media, { caption: caption || '' });
        console.log(`📄 PDF enviado: ${nombreArchivo}`);
        return true;
    } catch (error) {
        console.error(`❌ Error enviando PDF (${nombreArchivo}):`, error.message);
        return false;
    }
}

// ── Enviar texto al asesor ──
async function enviarTextoAsesor(numeroAsesor, mensaje) {
    try {
        const chatId = `${numeroAsesor}@c.us`;
        await client.sendMessage(chatId, mensaje);
        console.log(`📤 Resumen enviado al asesor`);
    } catch (error) {
        console.error('❌ Error enviando al asesor:', error.message);
    }
}

// CAMBIO 2: Función con retry — si Python no está listo, espera y reintenta
async function enviarAlBot(payload, reintentos = 3, espera = 2000) {
    for (let i = 0; i < reintentos; i++) {
        try {
            const response = await axios.post(PYTHON_BOT_URL, payload, { timeout: 10000 });
            return response;
        } catch (error) {
            if (i < reintentos - 1) {
                console.log(`⏳ Bot Python no disponible, reintentando (${i+1}/${reintentos})...`);
                await new Promise(r => setTimeout(r, espera));
            } else {
                throw error;
            }
        }
    }
}

// ── Recibir mensajes ──
client.on('message', async (msg) => {
    if (msg.isGroupMsg || msg.fromMe) return;

    const telefono = msg.from.replace('@c.us', '');
    const chatId   = msg.from;

    // CAMBIO 7: Detectar audios y mensajes de voz
    const tiposAudio = ['ptt', 'audio'];
    if (tiposAudio.includes(msg.type)) {
        try {
            const response = await enviarAlBot({
                from: telefono,
                body: '[AUDIO]',
                es_audio: true
            });
            const data = response.data;
            if (data.reply) await msg.reply(data.reply);
        } catch (error) {
            console.error('❌ Error procesando audio:', error.message);
        }
        return;
    }

    // Ignorar otros tipos de media (stickers, documentos, etc.) con mensaje amable
    if (msg.hasMedia && !['image','ptt','audio'].includes(msg.type)) {
        await msg.reply('Gracias por el archivo. Por ahora solo puedo procesar texto e imágenes. 😊');
        return;
    }

    // Ignorar imágenes (ya no se usan para el formulario)
    if (msg.hasMedia && msg.type === 'image') {
        await msg.reply('Gracias por la imagen. 😊\n\nPor favor escríbeme en texto para que pueda ayudarte mejor.');
        return;
    }

    const texto = msg.body;
    if (!texto || !texto.trim()) return;

    console.log(`📩 [${telefono}]: ${texto}`);

    try {
        const response = await enviarAlBot({
            from: telefono,
            body: texto
        });

        const data = response.data;

        // 1. Respuesta principal
        if (data.reply) {
            await msg.reply(data.reply);
            console.log(`🤖 Respondido a ${telefono}`);
        }

        // 2. Enviar PDF si Python lo indica
        if (data.enviar_pdf) {
            await new Promise(r => setTimeout(r, 800));
            await enviarPDF(chatId, data.enviar_pdf, data.caption_pdf || '');
        }

        // 3. Segundo mensaje de texto
        if (data.reply2) {
            await new Promise(r => setTimeout(r, 1500));
            await client.sendMessage(chatId, data.reply2);
        }

        // 4. Notificar al asesor
        if (data.notificar_asesor && data.numero_asesor && data.mensaje_asesor) {
            await enviarTextoAsesor(data.numero_asesor, data.mensaje_asesor);
        }

    } catch (error) {
        console.error('❌ Error al contactar el bot Python:', error.message);
        await msg.reply('Lo siento, dificultades técnicas momentáneas. Un asesor te contactará pronto. 🙏');
    }
});

// ── Endpoint: enviar texto ──
app.post('/send', async (req, res) => {
    const { phone, message } = req.body;
    if (!phone || !message) return res.status(400).json({ error: 'Faltan parámetros' });
    try {
        await client.sendMessage(`${phone}@c.us`, message);
        res.json({ success: true });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// ── Endpoint: enviar PDF ──
app.post('/send-pdf', async (req, res) => {
    const { phone, archivo, caption } = req.body;
    if (!phone || !archivo) return res.status(400).json({ error: 'Faltan parámetros' });
    try {
        const ok = await enviarPDF(`${phone}@c.us`, archivo, caption || '');
        res.json({ success: ok });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// ── Endpoint: estado ──
app.get('/status', (req, res) => {
    const archivos = fs.existsSync(PDFS_DIR)
        ? fs.readdirSync(PDFS_DIR).filter(f => f.endsWith('.pdf'))
        : [];
    res.json({
        connected: client.info ? true : false,
        pdfs_disponibles: archivos
    });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`🌐 Servidor Node.js en http://localhost:${PORT}`);
    console.log(`📂 PDFs en: ${PDFS_DIR}`);
});

client.initialize();
