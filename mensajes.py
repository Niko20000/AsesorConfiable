# ============================================================
# mensajes.py — Banco Caja Social / Alex Martínez
# ============================================================

NOMBRE_ASESOR = "Alex Martínez"
CARGO_ASESOR  = "Asesor Integral"
BANCO         = "Banco Caja Social"
OFICINA       = "Parque Principal Bello, Antioquia"
DIRECCION     = "Cr 49 49-03 Parque Principal Bello, Antioquia"
HORARIO       = "Lunes a viernes de 8:00 AM a 4:00 PM"
NUMERO_ASESOR = "573505494401"

# ─────────────────────────────────────────────
# TASAS VIGENTES — PROMEDIO M.V.
# ─────────────────────────────────────────────

TASAS_MV = {
    "1": {"nombre": "Crédito de Libre Inversión",    "tasa_mv": 1.5600, "desde_ea": 16.60, "hasta_ea": 24.25},
    "2": {"nombre": "Compra de Cartera",              "tasa_mv": 1.4650, "desde_ea": 14.35, "hasta_ea": 23.95},
    "3": {"nombre": "Crédito de Libranza",            "tasa_mv": 1.5300, "desde_ea": 15.00, "hasta_ea": 25.20},
    "4": {"nombre": "Libranza Compra de Cartera",     "tasa_mv": 1.5100, "desde_ea": 14.50, "hasta_ea": 25.20},
    "5": {"nombre": "Crédito Vivienda VIS",           "tasa_mv": 1.0650, "desde_ea": 11.90, "hasta_ea": 15.25},
    "6": {"nombre": "Crédito Vivienda NO VIS",        "tasa_mv": 1.1050, "desde_ea": 12.10, "hasta_ea": 16.10},
    "7": {"nombre": "Mejoramiento de Vivienda VIS",   "tasa_mv": 1.1800, "desde_ea": 14.40, "hasta_ea": 15.75},
    "8": {"nombre": "Mejoramiento de Vivienda NO VIS","tasa_mv": 1.2500, "desde_ea": 15.00, "hasta_ea": 17.15},
}

MAPA_SERVICIO_TASA = {
    "libre_inversion": "1",
    "compra_cartera":  "2",
    "libranza":        "3",
    "vivienda":        "5",
    "mejoramiento":    "7",
}

# ─────────────────────────────────────────────
# PDFs DISPONIBLES
# ─────────────────────────────────────────────

PDF_SEGUROS = {
    "1": {"archivo": "VIDA PROTEGIDA.pdf",        "caption": "📄 Información completa — *Vida Protegida*"},
    "2": {"archivo": "ACCIDENTES PERSONALES.pdf", "caption": "📄 Información completa — *Accidentes Personales Plus*"},
    "3": {"archivo": "PROTECCION DE AHORRO.pdf",  "caption": "📄 Información completa — *Protección de Ahorro*"},
    "4": {"archivo": "INGRESO PROTEGIDO.pdf",     "caption": "📄 Información completa — *Tu Ingreso Protegido*"},
    "5": {"archivo": "EXEQUIAL.pdf",              "caption": "📄 Información completa — *Seguro Exequial*"},
    "6": {"archivo": "DEVOLUCION DE PRIMA.pdf",   "caption": "📄 Información completa — *Vida con Devolución de Primas*"},
    "7": {"archivo": "TU CUOTA PROTEGIDA.pdf",    "caption": "📄 Información completa — *Tu Cuota Protegida*"},
    "8": {"archivo": "VIDA DEUDORES.pdf",         "caption": "📄 Información completa — *Vida Individual Deudores BCS*"},
    "9": {"archivo": "PROTECCION CRECIENTE.pdf",  "caption": "📄 Información completa — *Protección Creciente*"},
}

MSG_LISTA_PDFS = (
    "📎 *DOCUMENTOS DE NUESTROS SEGUROS*\n\n"
    "Escribe el número del seguro que te interesa y te lo envío de inmediato:\n\n"
    "1️⃣ Vida Protegida\n"
    "2️⃣ Accidentes Personales Plus\n"
    "3️⃣ Protección de Ahorro\n"
    "4️⃣ Tu Ingreso Protegido\n"
    "5️⃣ Seguro Exequial\n"
    "6️⃣ Vida con Devolución de Primas\n"
    "7️⃣ Tu Cuota Protegida\n"
    "8️⃣ Vida Individual Deudores BCS\n"
    "9️⃣ Protección Creciente\n\n"
    "Escribe *no* u *omitir* si no necesitas ninguno por ahora. 😊"
)

# Oferta proactiva de PDFs — se muestra después de dar info de un seguro
MSG_OFERTA_PDFS_PROACTIVA = (
    "¿Necesitas más información? 😊\n\n"
    "Tengo folletos completos en PDF de todos nuestros seguros para que "
    "puedas revisarlo con calma y tomar la mejor decisión:\n\n"
    "1️⃣ Vida Protegida  •  2️⃣ Accidentes Personales\n"
    "3️⃣ Protección de Ahorro  •  4️⃣ Ingreso Protegido\n"
    "5️⃣ Seguro Exequial  •  6️⃣ Vida c/Devolución\n"
    "7️⃣ Tu Cuota Protegida  •  8️⃣ Vida Deudores BCS\n"
    "9️⃣ Protección Creciente\n\n"
    "Escribe el número y te lo envío ahora mismo. 📄"
)

# Oferta de PDFs al final del formulario (cross-sell seguros)
MSG_OFERTA_PDFS_POST_SOLICITUD = (
    "📎 *¿Sabías que también protegemos tu crédito?*\n\n"
    "Tenemos seguros que cubren tus cuotas en caso de desempleo, "
    "incapacidad o cualquier imprevisto.\n\n"
    "Si quieres información de alguno, escríbeme el número:\n"
    "1️⃣ Vida Protegida  2️⃣ Accidentes  3️⃣ Protección de Ahorro\n"
    "4️⃣ Ingreso Protegido  7️⃣ Tu Cuota Protegida  9️⃣ Protección Creciente\n\n"
    "O escribe *no* para terminar. 😊"
)

# ─────────────────────────────────────────────
# SALUDO
# ─────────────────────────────────────────────

SALUDO_INICIAL = (
    "¡Hola! Buen día 😊 Mi nombre es *Alex Martínez* y soy Asesor Integral del *Banco Caja Social*.\n\n"
    "¿Con quién tengo el gusto? Me gustaría conocerte y saber en qué puedo ayudarte hoy."
)

def MSG_BIENVENIDA_NOMBRE(nombre):
    return (
        f"¡Mucho gusto, *{nombre}*! Es un placer atenderte. 😊\n\n"
        f"Cuéntame, ¿qué es lo que estás buscando hoy?\n"
        f"Estoy aquí para ayudarte con créditos, ahorro, inversión o seguros."
    )

# ─────────────────────────────────────────────
# PRESENTACIONES CÁLIDAS
# ─────────────────────────────────────────────

PRESENTACION_LIBRE_INVERSION = (
    "Sé que tienes metas por cumplir y quiero contarte que nuestro *Crédito de Libre Inversión* "
    "es el aliado perfecto para hacerlas realidad. Ya sea para iniciar ese proyecto que tienes "
    "en mente, financiar tus estudios, planear el viaje de tus sueños o simplemente cumplir ese "
    "deseo que tanto anhelas.\n\n"
    "*Requisitos:*\n"
    "• Edad entre 18 y 75 años\n"
    "• Afiliado a salud y pensión\n"
    "• Empleado, pensionado, rentista o independiente profesional\n"
    "• Ingresos desde 1 SMMLV\n\n"
    "¡Hablemos y busquemos la opción que mejor se adapte a ti! 😊"
)

PRESENTACION_LIBRANZA = (
    "Quiero contarte que tenemos una línea de *Crédito por Libranza* diseñada especialmente para usted.\n\n"
    "• *Pensionados:* COLPENSIONES, FOPEP, FOMAG, PENSIONES DE ANTIOQUIA, FIDUPREVISORA y más.\n"
    "• *Fuerzas Militares* (activos y retirados): EJÉRCITO, POLICÍA, ARMADA, CASUR, CREMIL y más.\n\n"
    "El banco lo acompaña para que pueda cumplir ese sueño que tiene pendiente — "
    "un viaje, estudios, un proyecto personal o unificar sus deudas.\n\n"
    "Es un proceso sencillo, *sin filas* y con cuotas que se adaptan a su pago mensual. 😊"
)

PRESENTACION_VIVIENDA = (
    "¿Sabías que el sueño de tener casa propia está más cerca de lo que crees? "
    "Queremos acompañarte a lograrlo a través de nuestras líneas:\n\n"
    "✅ *Crédito de Vivienda:* Para comprar casa nueva o usada.\n"
    "✅ *Mejoramiento de Vivienda:* Para remodelar y dejar tu hogar como siempre lo soñaste.\n"
    "✅ *Compra de Cartera de Vivienda:* Para mejorar las condiciones del crédito que tienes.\n\n"
    "Usted pone el sueño y nosotros ponemos el respaldo financiero. 🏠"
)

PRESENTACION_COMPRA_CARTERA = (
    "¿Sientes que las deudas te están quitando la tranquilidad? "
    "Quiero ayudarte a recuperar el control con nuestra *Compra de Cartera*.\n\n"
    "✅ Unificamos tus deudas en *una sola cuota mensual*.\n"
    "✅ Te ofrecemos una *mejor tasa de interés*.\n"
    "✅ Pagas menos cada mes para que vivas sin preocupaciones.\n\n"
    "¡Hablemos y empecemos a organizar tus finanzas hoy mismo! 🚀"
)

# ─────────────────────────────────────────────
# SIMULACIÓN AUTOMÁTICA
# ─────────────────────────────────────────────

def MSG_PRE_SIM_MONTO(nombre):
    """Si tenemos el nombre, lo usamos. Si no, omitirlo (no decir 'cliente')."""
    intro = f"Con mucho gusto, *{nombre}*. 😊\n\n" if nombre else "Con mucho gusto. 😊\n\n"
    return (
        intro +
        "Para que veas un ejemplo real de cómo te quedaría el crédito, "
        "cuéntame: ¿cuánto dinero necesitas aproximadamente?\n\n"
        "Puedes escribirlo como quieras: 5 millones, 500 mil, 2.000.000..."
    )

MSG_PRE_SIM_MESES = (
    "¿Y a cuántos meses te gustaría pagarlo? 📅\n\n"
    "Puedes elegir entre *12 y 240 meses*.\n"
    "Ejemplo: 12, 24, 36, 60, 120, 180..."
)

def MSG_PRE_SIM_RESULTADO(producto, monto_num, meses, tasa_mv, desde_ea, hasta_ea):
    r = tasa_mv / 100
    cuota = monto_num * r / (1 - (1 + r) ** (-meses))
    total_intereses = cuota * meses - monto_num

    def fmt(v):
        return f"${v:,.0f}".replace(",", ".")

    anos = meses // 12
    meses_rest = meses % 12
    if meses_rest == 0:
        plazo_str = f"{anos} {'año' if anos == 1 else 'años'}"
    elif anos > 0:
        plazo_str = f"{anos} años y {meses_rest} meses"
    else:
        plazo_str = f"{meses} meses"

    return (
        f"📊 *EJEMPLO REAL DE TU CRÉDITO*\n"
        f"──────────────────────────\n"
        f"💼 Producto: {producto}\n"
        f"💰 Monto: {fmt(monto_num)}\n"
        f"📅 Plazo: {plazo_str}\n"
        f"📈 Tasa promedio: {tasa_mv:.2f}% M.V.\n"
        f"──────────────────────────\n"
        f"💳 *Cuota mensual aprox:* *{fmt(cuota)}*\n"
        f"💵 Total a pagar: {fmt(cuota * meses)}\n"
        f"📉 Total en intereses: {fmt(total_intereses)}\n"
        f"──────────────────────────\n"
        f"⚠️ _Simulación referencial con tasa promedio. "
        f"La tasa real puede estar entre {desde_ea:.2f}% y {hasta_ea:.2f}% E.A. "
        f"según tu perfil — podría ser incluso mejor._\n\n"
        f"¿Te gustaría aplicar a este crédito?\n"
        f"Responde *Sí* para continuar o *No* si prefieres esperar. 😊"
    )

MSG_SIM_NO_APLICA = (
    "No hay ningún problema. 😊\n\n"
    "Cuando quieras retomar, aquí estaré con mucho gusto.\n\n"
    "📍 Cr 49 49-03 Parque Principal Bello | 🕒 Lun-Vie 8:00 AM - 4:00 PM"
)

MSG_CONFIRMAR_APLICAR = (
    "Disculpa, no te entendí bien. 😊\n\n"
    "¿Deseas aplicar a este crédito?\n"
    "Responde *Sí* para continuar o *No* si prefieres esperar."
)

SIMULADOR_MENU = (
    "Con mucho gusto hago la simulación. 😊\n\n"
    "¿Para qué tipo de crédito quieres simular?\n\n"
    "1️⃣ Crédito de Libre Inversión\n"
    "2️⃣ Compra de Cartera\n"
    "3️⃣ Crédito de Libranza\n"
    "4️⃣ Libranza Compra de Cartera\n"
    "5️⃣ Crédito Vivienda VIS\n"
    "6️⃣ Crédito Vivienda NO VIS\n"
    "7️⃣ Mejoramiento de Vivienda VIS\n"
    "8️⃣ Mejoramiento de Vivienda NO VIS\n\n"
    "Escribe solo el número 👆"
)

MSG_SIMULADOR_MONTO         = "¿Cuánto dinero necesitas? 💰\n\nEscríbelo como quieras: 5 millones, 500 mil, 2.000.000..."
MSG_SIMULADOR_MESES         = "¿A cuántos meses? 📅\n\nEntre *10 y 240 meses*. Ejemplo: 12, 24, 36, 60, 120..."
MSG_MESES_INVALIDOS         = "Por favor escribe un número entre *10 y 240* meses. 😊\nEjemplo: 12, 24, 36, 60, 120..."
MSG_SIMULADOR_PROD_INVALIDO = "Por favor escribe solo el número del producto (1 al 8). 😊"

def MSG_RESULTADO_SIMULACION(producto, monto_num, meses, tasa_mv, desde_ea, hasta_ea):
    return MSG_PRE_SIM_RESULTADO(producto, monto_num, meses, tasa_mv, desde_ea, hasta_ea)

# ─────────────────────────────────────────────
# AHORRO E INVERSIÓN
# ─────────────────────────────────────────────

AHORRO_PRESENTACION = (
    "¿Sabías que tu dinero puede trabajar para ti? "
    "Queremos que tus ahorros generen mejores rendimientos:\n\n"
    "📈 *CDT Tasa Fija:* Asegura una tasa fija y rentable.\n"
    "💰 *Cuentamiga Digital:* Hasta el *8.75% E.A.* de rentabilidad.\n"
    "🤝 *Fondo Rentafácil:* Inversiones a corto, mediano o largo plazo.\n\n"
    "¿Le gustaría que revisáramos qué opción le da más rentabilidad hoy? 😊"
)

AHORRO_INVITACION = (
    "Me encantaría invitarte personalmente a nuestra oficina en Bello para conversar "
    "sobre cómo hacer crecer tus ahorros con tasas competitivas y planes a tu medida.\n\n"
    "Será un gusto recibirte con un café ☕ y brindarte toda la información.\n\n"
    "📍 Cr 49 49-03 Parque Principal Bello, Antioquia.\n"
    "🕒 Lunes a viernes de 8:00 AM a 4:00 PM\n\n"
    "¿Qué día de esta semana te queda bien? 😊"
)

# ─────────────────────────────────────────────
# SEGUROS
# ─────────────────────────────────────────────

SEGUROS_PRESENTACION = (
    "¡Porque lo que más amas no tiene precio, pero sí protección! 💙🛡️\n\n"
    "En Banco Caja Social te cuidamos a ti, a tus finanzas y a tus seres queridos.\n\n"
    "👨‍👩‍👧‍👦 Seguros de vida, salud y exequial\n"
    "💳 Protección de tus productos financieros\n"
    "🏠 Respaldo para tu patrimonio"
)

SEGUROS_MENU = (
    "Escribe el *número* del seguro que te interesa y te envío la información completa con su PDF:\n\n"
    "1️⃣ *Vida Protegida* — Vida y enfermedades graves.\n"
    "2️⃣ *Accidentes Personales Plus* — Muerte e incapacidad.\n"
    "3️⃣ *Protección de Ahorro* — Desempleo o incapacidad.\n"
    "4️⃣ *Tu Ingreso Protegido* — Renta mensual hasta 6 meses.\n"
    "5️⃣ *Seguro Exequial* — Gastos exequiales.\n"
    "6️⃣ *Vida con Devolución de Primas* — Te devuelve el 50%.\n"
    "7️⃣ *Tu Cuota Protegida* — Cubre cuotas de tu crédito.\n"
    "8️⃣ *Vida Individual Deudores BCS* — Protege tu hipoteca.\n"
    "9️⃣ *Protección Creciente* — Vida y enfermedad grave."
)

SEGUROS_INVITACION = (
    "Para nosotros lo más importante es tu tranquilidad y la de tu familia. "
    "Me encantaría invitarte a nuestra oficina para que conozcas "
    "cómo nuestros seguros pueden proteger lo que más quieres, "
    "con planes que se ajustan perfectamente a tu bolsillo.\n\n"
    "Ven, nos tomamos un café ☕ y te brindo toda la información. ¡Te espero!\n\n"
    "📍 Cr 49 #49-03 (Parque Principal de Bello).\n"
    "🕒 Lunes a viernes de 8:00 AM a 4:00 PM.\n\n"
    "Pregunta directamente por mí, *Alex Martínez*, para darte atención preferencial. 😊"
)

SEGUROS_DETALLE = {
    "1": (
        "*Vida Protegida* 💙\n\n"
        "✅ Póliza inmediata — sin exámenes médicos\n"
        "✅ Muerte por cualquier causa\n"
        "✅ Enfermedad grave (Cáncer) — anticipo del 60%\n"
        "✅ Incapacidad total temporal — renta diaria de 4 a 180 días\n\n"
        "💰 Desde *$15.990* hasta *$40.990*/mes | 🎂 Edad: 18 a 60 años\n"
        "📞 Colmena Seguros: 601 4010447 / 018000919667 / #833"
    ),
    "2": (
        "*Accidentes Personales Plus* 🛡️\n\n"
        "✅ Póliza inmediata — sin exámenes médicos\n"
        "✅ Muerte por accidente — beneficiarios reciben el 100%\n"
        "✅ Incapacidad total y permanente por accidente\n\n"
        "💰 Desde *$4.990* hasta *$26.990* | 🎂 Edad: 18 a 65 años\n"
        "📞 Colmena Seguros: 601 4010447 / 018000919667 / #833"
    ),
    "3": (
        "*Protección de Ahorro* 💰\n\n"
        "✅ Póliza inmediata — sin exámenes médicos\n"
        "✅ Desempleo involuntario (asalariados)\n"
        "✅ Incapacidad temporal de 15+ días (independientes)\n\n"
        "💰 Desde *$5.000* hasta *$16.000*/mes | 🎂 Edad: 18 a 70 años\n"
        "📞 Colmena Seguros: 601 4010447 / 018000919667 / #833"
    ),
    "4": (
        "*Tu Ingreso Protegido* 💼\n\n"
        "✅ Renta mensual hasta 6 meses por desempleo o incapacidad\n"
        "✅ 6 mensualidades entre $500.000 y $1.200.000\n\n"
        "💰 Desde *$17.000* hasta *$35.000*/mes | 🎂 Edad: 18 a 70 años\n"
        "📞 Colmena Seguros: 601 4010447 / 018000919667 / #833"
    ),
    "5": (
        "*Seguro Exequial* 🕊️\n\n"
        "✅ Gastos exequiales para ti y tu familia\n"
        "✅ Plan Clásico (1-5 personas) o Extendido (1-8 personas)\n\n"
        "💰 Desde *$45.900* hasta *$661.200* | 🎂 Titular: 18 a 69 años\n"
        "📞 Colmena Seguros: 601 4010447 / 018000919667 / #833"
    ),
    "6": (
        "*Vida con Devolución de Primas* 🔄\n\n"
        "✅ Si sobrevives, te devolvemos el *50% de la prima* pagada\n"
        "✅ Cubre muerte por cualquier causa — vigencia 5 años\n\n"
        "💰 Desde *$150.000* hasta *$600.000* | 🎂 Edad: 18 a 59 años\n"
        "📞 Colmena Seguros: 601 4010447 / 018000919667 / #833"
    ),
    "7": (
        "*Tu Cuota Protegida* 🏦\n\n"
        "✅ Cubre cuotas del crédito en desempleo o incapacidad\n"
        "✅ Sin exámenes médicos\n\n"
        "Para valores exactos visítanos en la oficina. 😊\n"
        "📞 Colmena Seguros: 601 4010447 / 018000919667 / #833"
    ),
    "8": (
        "*Vida Individual Deudores BCS* 🏠\n\n"
        "✅ Cubre el *100% del saldo* de tu crédito hipotecario\n"
        "✅ Muerte, incapacidad, enfermedades graves, hospitalización\n\n"
        "🎂 Edad: 18 a 75 años\n"
        "📞 Línea Amiga: (601) 5426446 / 01 8000 910 038"
    ),
    "9": (
        "*Protección Creciente* 🌱\n\n"
        "✅ Póliza inmediata — sin exámenes médicos\n"
        "✅ Muerte, enfermedad grave e incapacidad total\n"
        "✅ El valor asegurado crece con la UVR\n\n"
        "💰 Desde *$8.800* hasta *$771.000* | 🎂 Edad: 18 a 65 años\n"
        "📞 Colmena Seguros: 601 4010447 / 018000919667 / #833"
    ),
}

# ─────────────────────────────────────────────
# FORMULARIO — MENSAJES
# ─────────────────────────────────────────────

MSG_PEDIR_NOMBRE  = "Para comenzar, ¿me podrías decir tu *nombre completo*? 😊"
MSG_RETRY_NOMBRE  = "Disculpa, no identifiqué bien tu nombre. 😊\n\n¿Me podrías decir tu *nombre completo* por favor?"

def MSG_PEDIR_CEDULA(nombre):
    return (
        f"¡Perfecto, *{nombre}*! Con mucho gusto. 😊\n\n"
        "¿Me podrías compartir tu número de *cédula*?"
    )

MSG_RETRY_CEDULA    = "No pude identificar la cédula. 😊\n\n¿Me la escribes como número?\nEjemplo: 1034567890"
MSG_PEDIR_INGRESOS  = "Gracias. 👍\n\n¿Cuáles son tus *ingresos mensuales* aproximados?\nCualquier monto es válido — aquí evaluamos cada caso con mucho gusto."
MSG_RETRY_INGRESOS  = "No pude entender el monto. 😊\n\nEjemplo: 1.500.000, 2 millones, 800 mil..."
MSG_PEDIR_ACTIVIDAD = "Gracias por compartirlo. 😊\n\n¿A qué te dedicas actualmente?\n(empleado, independiente, pensionado, fuerzas militares...)"
MSG_RETRY_ACTIVIDAD = "Disculpa, no entendí bien. 😊\n\n¿Me puedes contar a qué te dedicas?\nEjemplo: empleado en empresa privada, independiente, pensionado..."
MSG_PEDIR_ANTIGUEDAD = "Entendido. 🙌\n\n¿Cuánto tiempo llevas en esa actividad o empresa?\nPuedes indicarlo en meses o años."

def MSG_CONFIRMAR_ANTIGUEDAD(antiguedad):
    return (
        f"Solo para confirmar, 😊\n\n"
        f"¿cuando dices *{antiguedad}*, te refieres a ese tiempo exactamente?\n"
        f"Responde *Sí* para confirmar o escríbeme la corrección."
    )

MSG_PEDIR_CORREO   = "Ya casi terminamos. 📝\n\n¿Me das tu *correo electrónico*?"
MSG_RETRY_CORREO   = "No pude identificar el correo. 😊\n\nEjemplo: tunombre@gmail.com"
MSG_PEDIR_CELULAR  = "¿Y tu número de *celular*?\nNuestro asesor te contactará personalmente a este número. 😊"
MSG_RETRY_CELULAR  = "No pude reconocer el número. 😊\n\nEjemplo: 3001234567"

def MSG_RESUMEN(d):
    return (
        "Antes de finalizar, verifica que todo esté correcto:\n\n"
        f"👤 Nombre: {d.get('nombre', 'N/A')}\n"
        f"🪪 Cédula: {d.get('cedula', 'N/A')}\n"
        f"📞 Celular: {d.get('celular', 'N/A')}\n"
        f"📧 Correo: {d.get('correo', 'N/A')}\n"
        f"💰 Monto: {d.get('monto', 'N/A')}\n"
        f"📊 Ingresos: {d.get('ingresos', 'N/A')}\n"
        f"🏢 Actividad: {d.get('actividad', 'N/A')}\n"
        f"⏳ Antigüedad: {d.get('antiguedad', 'N/A')}\n\n"
        "¿Todo correcto? Responde *Sí* para finalizar o dime qué cambiar. 😊"
    )

MSG_CORREGIR_DATOS = "Claro que sí 😊 Dime qué dato quieres corregir.\nEjemplo: *cambiar nombre*, *cambiar monto*, etc."

# ─────────────────────────────────────────────
# CIERRE DE SOLICITUD — 2 MENSAJES FINALES
# ─────────────────────────────────────────────

def MSG_CIERRE_CALIDO(nombre_corto):
    """Mensaje 1: aviso cálido de que el asesor se comunica pronto."""
    saludo = f"¡*{nombre_corto}*," if nombre_corto else "¡Listo,"
    return (
        f"{saludo} tu solicitud ha sido registrada con éxito! 🎉\n\n"
        f"En unos momentos nuestro asesor *Alex Martínez* se comunicará contigo "
        f"personalmente para darte todos los detalles y continuar con el proceso.\n\n"
        f"Para agilizarlo, copia y envía el siguiente resumen directamente "
        f"por WhatsApp a este número:\n\n"
        f"👉 *+57 350 549 4401*"
    )

def MSG_RECIBO_FINAL(d):
    """Mensaje 2: recibo completo para que el cliente lo reenvíe al asesor."""
    return (
        "📋 *RESUMEN DE TU SOLICITUD*\n"
        "──────────────────────────\n"
        f"👤 Nombre: {d.get('nombre', 'N/A')}\n"
        f"🪪 Cédula: {d.get('cedula', 'N/A')}\n"
        f"📞 Celular: {d.get('celular', 'N/A')}\n"
        f"📧 Correo: {d.get('correo', 'N/A')}\n"
        f"💼 Producto: {d.get('servicio', 'N/A')}\n"
        f"💰 Monto: {d.get('monto', 'N/A')}\n"
        f"📊 Ingresos: {d.get('ingresos', 'N/A')}\n"
        f"🏢 Actividad: {d.get('actividad', 'N/A')}\n"
        f"⏳ Antigüedad: {d.get('antiguedad', 'N/A')}\n"
        "──────────────────────────\n"
        "🏦 *Banco Caja Social* — Oficina Bello\n"
        "📍 Cr 49 49-03 Parque Principal Bello\n"
        "🕒 Lun-Vie 8:00 AM - 4:00 PM\n\n"
        "📲 _Reenvía este mensaje a *+57 350 549 4401* para agilizar tu proceso_"
    )

def MSG_RESUMEN_ASESOR(d, numero_limpio):
    from datetime import datetime
    return (
        "🔔 *NUEVA SOLICITUD — BANCO CAJA SOCIAL*\n"
        "──────────────────────────\n"
        f"👤 Nombre: {d.get('nombre', 'N/A')}\n"
        f"🪪 Cédula: {d.get('cedula', 'N/A')}\n"
        f"📞 WhatsApp: +{numero_limpio}\n"
        f"📱 Celular: {d.get('celular', 'N/A')}\n"
        f"📧 Correo: {d.get('correo', 'N/A')}\n"
        f"💼 Producto: {d.get('servicio', 'N/A')}\n"
        f"💰 Monto: {d.get('monto', 'N/A')}\n"
        f"📊 Ingresos: {d.get('ingresos', 'N/A')}\n"
        f"🏢 Actividad: {d.get('actividad', 'N/A')}\n"
        f"⏳ Antigüedad: {d.get('antiguedad', 'N/A')}\n"
        "──────────────────────────\n"
        f"🗓️ {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    )

MSG_ERROR_TECNICO = "Disculpa, tuve un inconveniente técnico. Un asesor te contactará pronto. 🙏"

# ─────────────────────────────────────────────
# PROMPT DEL SISTEMA
# ─────────────────────────────────────────────

SISTEMA_PROMPT = f"""Eres {NOMBRE_ASESOR}, {CARGO_ASESOR} del {BANCO}, oficina de {OFICINA}.
Tienes un tono cálido, cercano y muy profesional — como un asesor bancario real.

SALUDO INICIAL:
"¡Hola! Buen día 😊 Mi nombre es Alex Martínez y soy Asesor Integral del Banco Caja Social.
¿Con quién tengo el gusto? Me gustaría conocerte y saber en qué puedo ayudarte hoy."

CUANDO SEPAS EL NOMBRE DEL CLIENTE, úsalo naturalmente y pregunta qué está buscando.
IMPORTANTE: NUNCA uses "cliente" como nombre. Si no sabes el nombre, no lo uses.

PRODUCTOS:

CRÉDITO DE LIBRE INVERSIÓN:
{PRESENTACION_LIBRE_INVERSION}

CRÉDITO DE LIBRANZA:
{PRESENTACION_LIBRANZA}

CRÉDITO DE VIVIENDA:
{PRESENTACION_VIVIENDA}

COMPRA DE CARTERA:
{PRESENTACION_COMPRA_CARTERA}

AHORRO E INVERSIÓN:
{AHORRO_PRESENTACION}
Invitación: {AHORRO_INVITACION}

SEGUROS:
{SEGUROS_PRESENTACION}
{SEGUROS_MENU}
Invitación: {SEGUROS_INVITACION}

DOCUMENTOS PDF DISPONIBLES:
Tenemos folletos PDF para todos los seguros (números 1 al 9).
Si el cliente pregunta por documentos, PDFs, folletos, catálogo o lista → responde: [MOSTRAR_PDFS]
Si el cliente escribe un número del 1 al 9, el sistema envía automáticamente la info y el PDF.

OFICINA: 📍 {DIRECCION} | 🕒 {HORARIO}

REGLAS:
1. Saluda como Alex Martínez del Banco Caja Social.
2. Usa el nombre del cliente naturalmente. NUNCA uses "cliente" si no sabes el nombre.
3. Cuando diga su nombre, salúdalo con calidez y pregunta qué busca.
4. Usa frases cálidas: "con mucho gusto", "es un placer", "no te preocupes".
5. Máximo 4 líneas por respuesta. Ve al punto.
6. 1 emoji al final.
7. NUNCA inventes tasas ni plazos exactos.
8. Si ingresos bajos o sin empleo: dile que igual se evalúa con mucho gusto.
9. Para CRÉDITOS: presenta cálidamente y termina con [INICIAR_CREDITO:tipo]
   tipos: libre_inversion, libranza, vivienda, compra_cartera
10. Para SIMULACIÓN: [INICIAR_SIMULADOR]
11. Para PDFs/documentos: [MOSTRAR_PDFS]
12. Para AHORRO/SEGUROS: invita a la oficina.

DETECTA crédito: quiero, necesito, préstamo, crédito, libranza, cartera, plata, dinero, cuotas, financiación.
DETECTA simulación: simular, calcular, cuánto pago, cuánto sería, cuánto me sale.
DETECTA PDFs: pdf, documento, folleto, brochure, información, lista, catálogo.

TONO: Cálido, profesional, genuinamente cercano.
"""