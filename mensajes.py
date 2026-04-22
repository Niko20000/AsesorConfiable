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
# FILTRO DE GROSERÍAS
# ─────────────────────────────────────────────

PALABRAS_GROSERAS = {
    "hijueputa","hijuepucha","gonorrea","malparido","malparida",
    "marica","maricon","puta","puto","mierda","culo","coño","verga",
    "culero","idiota","imbecil","imbécil","estupido","estúpido",
    "pendejo","pendeja","guevon","güevón","hp","hpta","hptm",
    "concha","chingado","cabron","cabrón","joder","mamahuevo","mamaguevo",
    "cerdo","cerda","perra","bestia","burro","burra",
    "estupida","estúpida","retrasado","retrasada",
    "maldito","maldita","desgraciado","desgraciada","infeliz",
    "fuck","shit","bitch","asshole","idiot","stupid","moron",
}

MSG_RESPUESTA_GROSER = (
    "Entiendo que quizás estás frustrado. Estoy aquí para ayudarte con mucho gusto. 😊\n\n"
    "Cuéntame en qué puedo servirte."
)

# ─────────────────────────────────────────────
# TASAS Y PLAZOS VIGENTES
# ─────────────────────────────────────────────

TASAS_MV = {
    "1": {"nombre": "Crédito de Libre Inversión",     "tasa_mv": 1.5600, "desde_ea": 16.60, "hasta_ea": 24.25, "min_meses": 12, "max_meses": 60},
    "2": {"nombre": "Compra de Cartera",               "tasa_mv": 1.4650, "desde_ea": 14.35, "hasta_ea": 23.95, "min_meses": 12, "max_meses": 60},
    "3": {"nombre": "Crédito de Libranza",             "tasa_mv": 1.5300, "desde_ea": 15.00, "hasta_ea": 25.20, "min_meses": 12, "max_meses": 140},
    "4": {"nombre": "Libranza Compra de Cartera",      "tasa_mv": 1.5100, "desde_ea": 14.50, "hasta_ea": 25.20, "min_meses": 12, "max_meses": 140},
    "5": {"nombre": "Crédito Hipotecario VIS",         "tasa_mv": 1.0650, "desde_ea": 11.90, "hasta_ea": 15.25, "min_meses": 12, "max_meses": 240},
    "6": {"nombre": "Crédito Hipotecario NO VIS",      "tasa_mv": 1.1050, "desde_ea": 12.10, "hasta_ea": 16.10, "min_meses": 12, "max_meses": 240},
    "7": {"nombre": "Mejoramiento de Vivienda VIS",    "tasa_mv": 1.1800, "desde_ea": 14.40, "hasta_ea": 15.75, "min_meses": 12, "max_meses": 120},
    "8": {"nombre": "Mejoramiento de Vivienda NO VIS", "tasa_mv": 1.2500, "desde_ea": 15.00, "hasta_ea": 17.15, "min_meses": 12, "max_meses": 120},
}

MAPA_SERVICIO_TASA = {
    "libre_inversion": "1",
    "compra_cartera":  "2",
    "libranza":        "3",
    "vivienda":        "5",
    "mejoramiento":    "7",
    "microcredito":    "1",  # usa tasa libre inversión como referencia
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
    "Escribe el número que te interesa:\n\n"
    "1️⃣ Vida Protegida\n"
    "2️⃣ Accidentes Personales Plus\n"
    "3️⃣ Protección de Ahorro\n"
    "4️⃣ Tu Ingreso Protegido\n"
    "5️⃣ Seguro Exequial\n"
    "6️⃣ Vida con Devolución de Primas\n"
    "7️⃣ Tu Cuota Protegida\n"
    "8️⃣ Vida Individual Deudores BCS\n"
    "9️⃣ Protección Creciente\n\n"
    "Escribe *0* si no necesitas ninguno. 😊"
)

MSG_OFERTA_PDFS_PROACTIVA = (
    "¿Quieres más información de algún seguro? 😊\n\n"
    "1️⃣ Vida Protegida  •  2️⃣ Accidentes\n"
    "3️⃣ Protección de Ahorro  •  4️⃣ Ingreso Protegido\n"
    "5️⃣ Exequial  •  6️⃣ Vida c/Devolución\n"
    "7️⃣ Tu Cuota Protegida  •  8️⃣ Vida Deudores\n"
    "9️⃣ Protección Creciente  •  *0* Para terminar"
)

MSG_OFERTA_PDFS_POST_SOLICITUD = (
    "📎 *¿Sabías que también protegemos tu crédito?*\n\n"
    "Tenemos seguros que cubren tus cuotas ante imprevistos.\n\n"
    "1️⃣ Vida Protegida  •  2️⃣ Accidentes\n"
    "3️⃣ Protección de Ahorro  •  7️⃣ Tu Cuota Protegida\n\n"
    "Escribe el número o *0* para terminar. 😊"
)

# ─────────────────────────────────────────────
# MENÚ INICIAL — CAMBIO 1
# ─────────────────────────────────────────────

MSG_MENU_INICIAL = (
    "¿Cómo puedo ayudarte hoy?\n\n"
    "1️⃣ Quiero información sobre productos y servicios\n"
    "2️⃣ Prefiero hablar directamente con un asesor\n\n"
    "Escribe *1* o *2*. 😊"
)

MSG_CONTACTO_DIRECTO = (
    "¡Con mucho gusto! 😊\n\n"
    "Puedes comunicarte directamente con nuestro asesor *Alex Martínez*:\n\n"
    "📱 *+57 350 549 4401*\n"
    "📍 Cr 49 49-03 Parque Principal Bello\n"
    "🕒 Lun-Vie 8:00 AM - 4:00 PM\n\n"
    "¡Te atenderemos con mucho gusto!"
)

# ─────────────────────────────────────────────
# MENÚ DE PRODUCTOS — CAMBIO 2
# ─────────────────────────────────────────────

MSG_MENU_PRODUCTOS = (
    "¿Qué te interesa? Escribe el número:\n\n"
    "1️⃣ Crédito de Libre Inversión\n"
    "2️⃣ Crédito de Libranza (pensionados y militares)\n"
    "3️⃣ Crédito de Vivienda\n"
    "4️⃣ Compra de Cartera\n"
    "5️⃣ Microcrédito para independientes\n"
    "6️⃣ Ahorro e Inversión\n"
    "7️⃣ Seguros\n"
    "8️⃣ Simular cuota de crédito 📊"
)

# Mapeo de opción del menú a acción interna
MENU_OPCIONES = {
    "1": "credito_libre",
    "2": "credito_libranza",
    "3": "credito_vivienda",
    "4": "compra_cartera",
    "5": "microcredito",
    "6": "ahorro",
    "7": "seguros",
    "8": "simulador",
}

# ─────────────────────────────────────────────
# MENÚ DE ACTIVIDAD — CAMBIO 2
# ─────────────────────────────────────────────

MSG_PEDIR_ACTIVIDAD = (
    "¿A qué te dedicas actualmente? Escribe el número:\n\n"
    "1️⃣ Empleado\n"
    "2️⃣ Independiente\n"
    "3️⃣ Pensionado\n"
    "4️⃣ Rentista de capital\n"
    "5️⃣ Transportador\n"
    "6️⃣ Otra actividad (escríbela a continuación)"
)

ACTIVIDAD_OPCIONES = {
    "1": "Empleado",
    "2": "Independiente",
    "3": "Pensionado",
    "4": "Rentista de capital",
    "5": "Transportador",
}

MSG_RETRY_ACTIVIDAD = (
    "Disculpa, no entendí. 😊\n\n"
    "Escribe el número de tu actividad:\n\n"
    "1️⃣ Empleado  •  2️⃣ Independiente\n"
    "3️⃣ Pensionado  •  4️⃣ Rentista de capital\n"
    "5️⃣ Transportador  •  6️⃣ Otra (escríbela)"
)

# ─────────────────────────────────────────────
# SALUDO
# ─────────────────────────────────────────────

SALUDO_INICIAL = (
    "¡Hola! Buen día 😊 Soy *Alex Martínez*, Asesor Integral del *Banco Caja Social*.\n\n"
    "¿Con quién tengo el gusto?"
)

def MSG_BIENVENIDA_NOMBRE(nombre):
    return (
        f"¡Mucho gusto, *{nombre}*! Es un placer atenderte. 😊\n\n"
        + MSG_MENU_INICIAL
    )

# ─────────────────────────────────────────────
# PRESENTACIONES DE PRODUCTOS
# ─────────────────────────────────────────────

PRESENTACION_LIBRE_INVERSION = (
    "Nuestro *Crédito de Libre Inversión* es perfecto para cumplir tus metas — "
    "estudios, viajes, proyectos o lo que necesites.\n\n"
    "*Requisitos:*\n"
    "• Edad 18 a 75 años | Afiliado a salud y pensión\n"
    "• Empleado, pensionado, rentista o independiente profesional\n"
    "• Ingresos desde 1 SMMLV | Plazo: 12 a 60 meses\n\n"
    "*Recuerda:* Empleados, pensionados, rentistas de capital y transportadores "
    "pueden acceder a mejores condiciones. 😊"
)

PRESENTACION_MICROCREDITO = (
    "Para independientes tenemos una línea especial de *Microcrédito* "
    "diseñada para impulsar tu negocio o actividad.\n\n"
    "✅ Sin necesidad de historial crediticio extenso\n"
    "✅ Montos desde 1 SMMLV\n"
    "✅ Proceso ágil y personalizado\n\n"
    "*Recuerda:* Si eres independiente, transportador o tienes tu propio negocio, "
    "esta es tu mejor opción. Un asesor evaluará tu caso con mucho gusto. 😊"
)

PRESENTACION_LIBRANZA = (
    "Nuestro *Crédito por Libranza* está diseñado especialmente para:\n\n"
    "• *Pensionados:* COLPENSIONES, FOPEP, FOMAG, FIDUPREVISORA y más.\n"
    "• *Militares activos y retirados:* EJÉRCITO, POLICÍA, ARMADA, CASUR, CREMIL y más.\n\n"
    "✅ Descuento directo de nómina o mesada | Sin codeudores\n"
    "✅ Plazo: 12 a 140 meses | Proceso sin filas\n\n"
    "*Recuerda:* Pensionados de fondos públicos y privados tienen condiciones preferenciales. 😊"
)

PRESENTACION_VIVIENDA = (
    "Cumple el sueño de tener casa propia con nuestras líneas:\n\n"
    "✅ *Crédito Hipotecario:* Casa nueva o usada — hasta 240 meses en Pesos / 300 en UVR\n"
    "✅ *Mejoramiento de Vivienda:* Para remodelar — hasta 120 meses\n"
    "✅ *Compra de Cartera de Vivienda:* Mejora tu crédito actual\n\n"
    "• Aplican subsidios del gobierno\n"
    "• Puedes sumar ingresos con otro solicitante\n\n"
    "*Recuerda:* Empleados con antigüedad y pensionados tienen mejores tasas. 🏠"
)

PRESENTACION_COMPRA_CARTERA = (
    "Con nuestra *Compra de Cartera* unificamos tus deudas en una sola cuota con mejor tasa.\n\n"
    "✅ Menos intereses | Mayor liquidez | Plazo: 12 a 60 meses\n\n"
    "*Recuerda:* Empleados, pensionados y rentistas acceden a las mejores condiciones. 🚀"
)

# ─────────────────────────────────────────────
# SIMULACIÓN
# ─────────────────────────────────────────────

def MSG_PRE_SIM_MONTO(nombre):
    intro = f"Con mucho gusto, *{nombre}*. 😊\n\n" if nombre else "Con mucho gusto. 😊\n\n"
    return intro + "¿Cuánto dinero necesitas aproximadamente?\n\nEjemplo: 5 millones, 500 mil, 2.000.000..."

def MSG_PRE_SIM_MESES(min_m, max_m):
    return (
        f"¿A cuántos meses te gustaría pagarlo? 📅\n\n"
        f"Para este producto el plazo es de *{min_m} a {max_m} meses*.\n"
        f"Ejemplo: {min_m}, {min_m*2}, {min_m*3}..."
    )

MSG_PRE_SIM_MESES_DEFAULT = (
    "¿A cuántos meses te gustaría pagarlo? 📅\n\n"
    "Ejemplo: 12, 24, 36, 60..."
)

def MSG_PRE_SIM_RESULTADO(producto, monto_num, meses, tasa_mv, desde_ea, hasta_ea):
    r = tasa_mv / 100
    cuota = monto_num * r / (1 - (1 + r) ** (-meses))

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
        f"📊 *EJEMPLO REAL*\n"
        f"──────────────────────\n"
        f"💼 {producto}\n"
        f"💰 Monto: {fmt(monto_num)}\n"
        f"📅 Plazo: {plazo_str}\n"
        f"──────────────────────\n"
        f"💳 *Cuota aprox: {fmt(cuota)}/mes*\n"
        f"──────────────────────\n"
        f"⚠️ _Tasa promedio {tasa_mv:.2f}% M.V. "
        f"La real puede estar entre {desde_ea:.2f}% y {hasta_ea:.2f}% E.A. según tu perfil._\n\n"
        f"¿Quieres aplicar?\n"
        f"*Sí* para continuar | *No* para esperar 😊"
    )

def MSG_SIM_SEGURO(nombre_seguro, plan_desde, plan_hasta):
    return (
        f"📊 *{nombre_seguro.upper()}*\n"
        f"──────────────────────\n"
        f"💰 Planes desde: *{plan_desde}*\n"
        f"💰 Planes hasta: *{plan_hasta}*\n"
        f"✅ Póliza inmediata — sin exámenes médicos\n"
        f"✅ Emitido por *Colmena Seguros*\n\n"
        f"⚠️ _Valor exacto depende del plan y cobertura._\n\n"
        f"¿Registramos tu interés para que te contactemos?\n"
        f"*Sí* para continuar | *No* para esperar 😊"
    )

def MSG_SIM_AHORRO(monto_num, dias):
    tasa_ea = 0.0875
    rendimiento = monto_num * ((1 + tasa_ea) ** (dias / 365) - 1)

    def fmt(v):
        return f"${v:,.0f}".replace(",", ".")

    return (
        f"📊 *EJEMPLO REAL — AHORRO*\n"
        f"──────────────────────\n"
        f"💰 Inversión: {fmt(monto_num)}\n"
        f"📅 Plazo: {dias} días\n"
        f"📈 Tasa ref: 8.75% E.A. (Cuentamiga)\n"
        f"──────────────────────\n"
        f"💵 *Rendimiento aprox: {fmt(rendimiento)}*\n\n"
        f"⚠️ _Varía según producto y plazo._\n\n"
        f"¿Quieres que un asesor te muestre las opciones?\n"
        f"*Sí* para continuar | *No* para esperar 😊"
    )

SEGUROS_PLANES = {
    "1": {"nombre": "Vida Protegida",        "desde": "$15.990/mes", "hasta": "$40.990/mes"},
    "2": {"nombre": "Accidentes Personales", "desde": "$4.990",      "hasta": "$26.990"},
    "3": {"nombre": "Protección de Ahorro",  "desde": "$5.000/mes",  "hasta": "$16.000/mes"},
    "4": {"nombre": "Tu Ingreso Protegido",  "desde": "$17.000/mes", "hasta": "$35.000/mes"},
    "5": {"nombre": "Seguro Exequial",       "desde": "$45.900",     "hasta": "$661.200"},
    "6": {"nombre": "Vida con Devolución",   "desde": "$150.000",    "hasta": "$600.000"},
    "7": {"nombre": "Tu Cuota Protegida",    "desde": "según plan",  "hasta": "según plan"},
    "8": {"nombre": "Vida Deudores BCS",     "desde": "según plan",  "hasta": "según plan"},
    "9": {"nombre": "Protección Creciente",  "desde": "$8.800",      "hasta": "$771.000"},
}

MSG_SIM_NO_APLICA = (
    "No hay problema. Cuando quieras, aquí estaré. 😊\n\n"
    "📍 Cr 49 49-03 Parque Principal Bello | 🕒 Lun-Vie 8:00 AM - 4:00 PM"
)

MSG_CONFIRMAR_APLICAR = (
    "Disculpa, no te entendí. 😊\n\n"
    "¿Deseas continuar?\n"
    "*Sí* para continuar | *No* para esperar"
)

SIMULADOR_MENU = (
    "¿Para qué producto quieres simular? Escribe el número:\n\n"
    "1️⃣ Libre Inversión (12-60 meses)\n"
    "2️⃣ Compra de Cartera (12-60 meses)\n"
    "3️⃣ Libranza (12-140 meses)\n"
    "4️⃣ Libranza C.Cartera (12-140 meses)\n"
    "5️⃣ Hipotecario VIS (12-240 meses)\n"
    "6️⃣ Hipotecario NO VIS (12-240 meses)\n"
    "7️⃣ Mejoramiento VIS (12-120 meses)\n"
    "8️⃣ Mejoramiento NO VIS (12-120 meses)"
)

MSG_SIMULADOR_MONTO         = "¿Cuánto dinero necesitas? 💰\n\nEjemplo: 5 millones, 500 mil, 2.000.000..."
MSG_SIMULADOR_MESES_BASE    = "¿A cuántos meses? 📅\n\nEjemplo: 12, 24, 36, 60..."
MSG_MESES_INVALIDOS         = "Por favor escribe un número de meses válido para este producto. 😊"
MSG_SIMULADOR_PROD_INVALIDO = "Escribe solo el número del producto (1 al 8). 😊"

def MSG_RESULTADO_SIMULACION(producto, monto_num, meses, tasa_mv, desde_ea, hasta_ea):
    return MSG_PRE_SIM_RESULTADO(producto, monto_num, meses, tasa_mv, desde_ea, hasta_ea)

# ─────────────────────────────────────────────
# AHORRO E INVERSIÓN
# ─────────────────────────────────────────────

AHORRO_PRESENTACION = (
    "Haz crecer tu dinero con nosotros:\n\n"
    "📈 *CDT Tasa Fija:* Tasa fija garantizada.\n"
    "💰 *Cuentamiga Digital:* Hasta *8.75% E.A.* de rentabilidad.\n"
    "🤝 *Fondo Rentafácil:* Bajo riesgo, liquidez diaria.\n\n"
    "¿Quieres ver un ejemplo de cuánto podrías ganar? 😊"
)

AHORRO_INVITACION = (
    "Me encantaría mostrarte cómo hacer crecer tus ahorros. ☕\n\n"
    "📍 Cr 49 49-03 Parque Principal Bello\n"
    "🕒 Lun-Vie 8:00 AM - 4:00 PM\n\n"
    "¿Qué día te queda bien visitarme? 😊"
)

# ─────────────────────────────────────────────
# SEGUROS
# ─────────────────────────────────────────────

SEGUROS_PRESENTACION = (
    "¡Protege lo que más amas! 💙🛡️\n\n"
    "En Banco Caja Social tenemos seguros para ti y tu familia.\n\n"
    "Escribe el número que te interesa:\n\n"
    "1️⃣ Vida Protegida  •  2️⃣ Accidentes Personales\n"
    "3️⃣ Protección de Ahorro  •  4️⃣ Tu Ingreso Protegido\n"
    "5️⃣ Seguro Exequial  •  6️⃣ Vida c/Devolución de Primas\n"
    "7️⃣ Tu Cuota Protegida  •  8️⃣ Vida Deudores BCS\n"
    "9️⃣ Protección Creciente"
)

SEGUROS_MENU = SEGUROS_PRESENTACION

SEGUROS_INVITACION = (
    "¡Te espero en nuestra oficina para conocer el seguro ideal para ti! ☕\n\n"
    "📍 Cr 49 #49-03 Parque Principal Bello\n"
    "🕒 Lun-Vie 8:00 AM - 4:00 PM\n\n"
    "Pregunta por *Alex Martínez*. 😊"
)

SEGUROS_DETALLE = {
    "1": (
        "*Vida Protegida* 💙\n\n"
        "✅ Póliza inmediata — sin exámenes\n"
        "✅ Muerte, cáncer (anticipo 60%) e incapacidad\n\n"
        "💰 Desde *$15.990* hasta *$40.990*/mes\n"
        "🎂 Edad: 18 a 60 años\n"
        "📞 Colmena: 601 4010447 / 018000919667 / #833"
    ),
    "2": (
        "*Accidentes Personales Plus* 🛡️\n\n"
        "✅ Póliza inmediata — sin exámenes\n"
        "✅ Muerte por accidente + incapacidad permanente\n\n"
        "💰 Desde *$4.990* hasta *$26.990*\n"
        "🎂 Edad: 18 a 65 años\n"
        "📞 Colmena: 601 4010447 / 018000919667 / #833"
    ),
    "3": (
        "*Protección de Ahorro* 💰\n\n"
        "✅ Protege tu ahorro en desempleo o incapacidad\n"
        "✅ Sin exámenes médicos\n\n"
        "💰 Desde *$5.000* hasta *$16.000*/mes\n"
        "🎂 Edad: 18 a 70 años\n"
        "📞 Colmena: 601 4010447 / 018000919667 / #833"
    ),
    "4": (
        "*Tu Ingreso Protegido* 💼\n\n"
        "✅ Renta mensual hasta 6 meses\n"
        "✅ Por desempleo o incapacidad\n\n"
        "💰 Desde *$17.000* hasta *$35.000*/mes\n"
        "🎂 Edad: 18 a 70 años\n"
        "📞 Colmena: 601 4010447 / 018000919667 / #833"
    ),
    "5": (
        "*Seguro Exequial* 🕊️\n\n"
        "✅ Cubre gastos exequiales para ti y tu familia\n"
        "✅ Plan Clásico (1-5) o Extendido (1-8 personas)\n\n"
        "💰 Desde *$45.900* hasta *$661.200*\n"
        "📞 Colmena: 601 4010447 / 018000919667 / #833"
    ),
    "6": (
        "*Vida con Devolución de Primas* 🔄\n\n"
        "✅ Si sobrevives, te devolvemos el *50% de la prima*\n"
        "✅ Vigencia 5 años — prima única\n\n"
        "💰 Desde *$150.000* hasta *$600.000*\n"
        "🎂 Edad: 18 a 59 años\n"
        "📞 Colmena: 601 4010447 / 018000919667 / #833"
    ),
    "7": (
        "*Tu Cuota Protegida* 🏦\n\n"
        "✅ Cubre cuotas de tu crédito en desempleo\n"
        "✅ Sin exámenes médicos\n\n"
        "Para valores exactos visítanos. 😊\n"
        "📞 Colmena: 601 4010447 / 018000919667 / #833"
    ),
    "8": (
        "*Vida Individual Deudores BCS* 🏠\n\n"
        "✅ Cubre el *100% del saldo* hipotecario\n"
        "✅ Muerte, incapacidad y enfermedades graves\n\n"
        "🎂 Edad: 18 a 75 años\n"
        "📞 Línea Amiga: (601) 5426446 / 01 8000 910 038"
    ),
    "9": (
        "*Protección Creciente* 🌱\n\n"
        "✅ Vida, enfermedad grave e incapacidad total\n"
        "✅ El valor asegurado crece con la UVR\n\n"
        "💰 Desde *$8.800* hasta *$771.000*\n"
        "🎂 Edad: 18 a 65 años\n"
        "📞 Colmena: 601 4010447 / 018000919667 / #833"
    ),
}

# ─────────────────────────────────────────────
# FORMULARIO — MENSAJES CORTOS Y CONCRETOS
# ─────────────────────────────────────────────

MSG_PEDIR_NOMBRE  = "¿Me podrías decir tu *nombre completo*? 😊"
MSG_RETRY_NOMBRE  = "No identifiqué tu nombre. 😊\n\n¿Me lo escribes completo por favor?"

def MSG_PEDIR_CEDULA(nombre):
    return f"Mucho gusto, *{nombre}*. 😊\n\n¿Cuál es tu número de *cédula*?"

MSG_RETRY_CEDULA   = "No pude identificar la cédula. 😊\n\nEjemplo: 1034567890"
MSG_PEDIR_INGRESOS = "¿Cuáles son tus *ingresos mensuales* aproximados? 👍\n\nCualquier monto es válido."
MSG_RETRY_INGRESOS = "No entendí el monto. 😊\n\nEjemplo: 1.500.000, 2 millones, 800 mil..."

# MSG_PEDIR_ACTIVIDAD está arriba (menú numerado)

# CAMBIO 3: Antigüedad solo en años
MSG_PEDIR_ANTIGUEDAD = (
    "¿Cuántos *años* llevas en esa actividad o empresa? 🙌\n\n"
    "Escribe solo el número de años. Ejemplo: 2, 5, 10..."
)

MSG_RETRY_ANTIGUEDAD = (
    "Por favor escribe el número de *años* que llevas en esa actividad. 😊\n\n"
    "Ejemplo: 1, 3, 5, 10..."
)

def MSG_CONFIRMAR_ANTIGUEDAD(antiguedad):
    return (
        f"¿Llevas *{antiguedad}* en esa actividad?\n"
        f"*Sí* para confirmar o escríbeme la corrección. 😊"
    )

MSG_PEDIR_CORREO  = "¿Cuál es tu *correo electrónico*? 📝"
MSG_RETRY_CORREO  = "No identifiqué el correo. 😊\n\nEjemplo: tunombre@gmail.com"
MSG_PEDIR_CELULAR = "¿Y tu número de *celular*? Nuestro asesor te contactará ahí. 😊"
MSG_RETRY_CELULAR = "No reconocí el número. 😊\n\nEjemplo: 3001234567"

def MSG_RESUMEN(d):
    return (
        "Verifica que todo esté correcto:\n\n"
        f"👤 {d.get('nombre', 'N/A')}\n"
        f"🪪 {d.get('cedula', 'N/A')}\n"
        f"📞 {d.get('celular', 'N/A')}\n"
        f"📧 {d.get('correo', 'N/A')}\n"
        f"💼 {d.get('servicio_nombre', d.get('servicio', 'N/A'))}\n"
        f"💰 {d.get('monto', 'N/A')}\n"
        f"📊 Ingresos: {d.get('ingresos', 'N/A')}\n"
        f"🏢 {d.get('actividad', 'N/A')}\n"
        f"⏳ Antigüedad: {d.get('antiguedad', 'N/A')}\n\n"
        "*Sí* para finalizar | Dime qué cambiar 😊"
    )

MSG_CORREGIR_DATOS = "Dime qué quieres corregir. 😊\nEjemplo: *cambiar monto*, *cambiar correo*..."

# ─────────────────────────────────────────────
# CIERRE
# ─────────────────────────────────────────────

def MSG_CIERRE_CALIDO(nombre_corto):
    saludo = f"¡*{nombre_corto}*," if nombre_corto else "¡Listo,"
    return (
        f"{saludo} tu solicitud fue registrada con éxito! 🎉\n\n"
        f"*Alex Martínez* te contactará pronto para continuar.\n\n"
        f"Para agilizarlo, envía el resumen siguiente a:\n"
        f"👉 *+57 350 549 4401*"
    )

def MSG_RECIBO_FINAL(d):
    return (
        "📋 *RESUMEN DE TU SOLICITUD*\n"
        "──────────────────────\n"
        f"👤 {d.get('nombre', 'N/A')}\n"
        f"🪪 {d.get('cedula', 'N/A')}\n"
        f"📞 {d.get('celular', 'N/A')}\n"
        f"📧 {d.get('correo', 'N/A')}\n"
        f"💼 {d.get('servicio_nombre', d.get('servicio', 'N/A'))}\n"
        f"💰 {d.get('monto', 'N/A')}\n"
        f"📊 Ingresos: {d.get('ingresos', 'N/A')}\n"
        f"🏢 {d.get('actividad', 'N/A')}\n"
        f"⏳ Antigüedad: {d.get('antiguedad', 'N/A')}\n"
        "──────────────────────\n"
        "🏦 *Banco Caja Social* — Bello\n"
        "📍 Cr 49 49-03 Parque Principal\n"
        "🕒 Lun-Vie 8:00 AM - 4:00 PM\n\n"
        "📲 _Reenvía este mensaje a *+57 350 549 4401*_"
    )

def MSG_RESUMEN_ASESOR(d, numero_limpio):
    from datetime import datetime
    return (
        "🔔 *NUEVA SOLICITUD — BCS*\n"
        "──────────────────────\n"
        f"👤 {d.get('nombre', 'N/A')}\n"
        f"🪪 {d.get('cedula', 'N/A')}\n"
        f"📞 WA: +{numero_limpio}\n"
        f"📱 Cel: {d.get('celular', 'N/A')}\n"
        f"📧 {d.get('correo', 'N/A')}\n"
        f"💼 {d.get('servicio_nombre', d.get('servicio', 'N/A'))}\n"
        f"💰 {d.get('monto', 'N/A')}\n"
        f"📊 Ingresos: {d.get('ingresos', 'N/A')}\n"
        f"🏢 {d.get('actividad', 'N/A')}\n"
        f"⏳ Antigüedad: {d.get('antiguedad', 'N/A')}\n"
        "──────────────────────\n"
        f"🗓️ {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    )

MSG_ERROR_TECNICO      = "Disculpa, inconveniente técnico. Un asesor te contactará pronto. 🙏"
MSG_AUDIO_NO_SOPORTADO = "Disculpa, no puedo escuchar audios por el momento. 😊\n\nCuéntame en texto en qué puedo ayudarte."

# ─────────────────────────────────────────────
# PROMPT DEL SISTEMA
# ─────────────────────────────────────────────

SISTEMA_PROMPT = f"""Eres {NOMBRE_ASESOR}, {CARGO_ASESOR} del {BANCO}, oficina de {OFICINA}.
Tono: cálido, concreto y profesional. Respuestas cortas — máximo 4 líneas. 1 emoji al final.

SALUDO INICIAL:
"¡Hola! Buen día 😊 Soy *Alex Martínez*, Asesor Integral del *Banco Caja Social*.
¿Con quién tengo el gusto?"

CUANDO SEPAS EL NOMBRE: saluda con calidez y muestra el menú de opciones.
NUNCA uses "cliente" si no sabes el nombre.
Si el cliente usa groserías: responde con calma, nunca las repitas.

PRODUCTOS Y PLAZOS:
- Libre Inversión: 12-60 meses
- Compra de Cartera: 12-60 meses
- Libranza: 12-140 meses
- Hipotecario: 12-240 meses (Pesos) / 300 meses (UVR)
- Mejoramiento Vivienda: 12-120 meses
- Microcrédito: para independientes y transportadores

MENÚ PRINCIPAL (mostrar cuando el cliente quiere información):
{MSG_MENU_PRODUCTOS}

REGLAS:
1. Respuestas cortas y directas. Máximo 4 líneas.
2. Usa menús numerados siempre que sea posible.
3. NUNCA inventes tasas exactas.
4. Si ingresos bajos: dile que igual se evalúa su caso.
5. Para CRÉDITOS: responde [INICIAR_CREDITO:tipo]
   tipos: libre_inversion, libranza, vivienda, compra_cartera, microcredito
6. Para SEGUROS: responde [INICIAR_SEGURO:numero]
7. Para AHORRO: responde [INICIAR_AHORRO]
8. Para SIMULACIÓN: [INICIAR_SIMULADOR]
9. Para PDFs: [MOSTRAR_PDFS]
10. Para contacto directo con asesor: muestra número y dirección.

DETECTA crédito: préstamo, crédito, libranza, cartera, plata, dinero, cuotas, financiación, microcrédito.
DETECTA simulación: simular, calcular, cuánto pago, cuánto sería, cuánto me sale.

TONO: Cálido, directo, genuinamente cercano.
"""