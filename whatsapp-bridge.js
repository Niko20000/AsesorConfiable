/**
 * Puente WhatsApp → Python
 * - Recibe mensajes de texto
 * - Envía PDFs de productos automáticamente al cliente
 * - Notifica al asesor con resúmenes de solicitudes
 */

const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const axios  = require('axios');
const express = require('express');
const fs   = require('fs');
const path = require('path');

const app = express();
app.use(express.json({ limit: '50mb' }));

const PYTHON_BOT_URL = 'http://localhost:5000/mensaje';
const PDFS_DIR = path.join(__dirname, 'pdfs');  // ← pon aquí tus PDFs

// Crear carpeta pdfs si no existe
if (!fs.existsSync(PDFS_DIR)) {
    fs.mkdirSync(PDFS_DIR, { recursive: true });
    console.log(`📂 Carpeta creada: ${PDFS_DIR}`);
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
    console.log(`📂 PDFs disponibles en: ${PDFS_DIR}`);
    // Listar PDFs disponibles al arrancar
    try {
        const archivos = fs.readdirSync(PDFS_DIR).filter(f => f.endsWith('.pdf'));
        if (archivos.length > 0) {
            console.log(`📄 PDFs cargados: ${archivos.join(', ')}`);
        } else {
            console.log('⚠️  No hay PDFs en la carpeta /pdfs/ todavía.');
        }
    } catch(e) {}
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

// ── Recibir mensajes ──
client.on('message', async (msg) => {
    if (msg.isGroupMsg || msg.fromMe) return;

    const telefono = msg.from.replace('@c.us', '');
    const chatId   = msg.from;

    // Si el cliente envía una imagen u otro archivo, ignorar con mensaje amable
    if (msg.hasMedia) {
        const media = await msg.downloadMedia().catch(() => null);
        if (media && media.mimetype && !media.mimetype.startsWith('image/')) {
            // Es un documento, ignorar
            return;
        }
        // Es una imagen — responder con mensaje amable
        await msg.reply('Gracias por el archivo. Un asesor lo revisará pronto. 😊');
        return;
    }

    const texto = msg.body;
    console.log(`📩 [${telefono}]: ${texto}`);

    try {
        const response = await axios.post(PYTHON_BOT_URL, {
            from: telefono,
            body: texto
        });

        const data = response.data;

        // 1. Respuesta principal de texto
        if (data.reply) {
            await msg.reply(data.reply);
            console.log(`🤖 Respondido a ${telefono}`);
        }

        // 2. Enviar PDF del producto si Python lo indica
        if (data.enviar_pdf) {
            await new Promise(r => setTimeout(r, 800)); // pausa natural antes del PDF
            await enviarPDF(chatId, data.enviar_pdf, data.caption_pdf || '');
        }

        // 3. Segundo mensaje de texto (instrucción de reenvío al asesor)
        if (data.reply2) {
            await new Promise(r => setTimeout(r, 1500));
            await client.sendMessage(chatId, data.reply2);
        }

        // 4. Notificar al asesor con el resumen
        if (data.notificar_asesor && data.numero_asesor && data.mensaje_asesor) {
            await enviarTextoAsesor(data.numero_asesor, data.mensaje_asesor);
        }

    } catch (error) {
        console.error('❌ Error al contactar el bot Python:', error.message);
        await msg.reply('Lo siento, dificultades técnicas. Un asesor te contactará pronto. 🙏');
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

// ── Endpoint: enviar PDF manualmente ──
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
});

client.initialize();