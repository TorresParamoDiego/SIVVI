# base_conocimiento.py
# Contiene la base de preguntas del sistema experto.

base_de_conocimiento = {
    "1": {
        "pregunta": "¿Tienes moretones o marcas que no puedes explicar después de convivir con esa persona?",
        "hipotesis": [("violencia_fisica", 0.92), ("violencia_psicologica", 0.22)]
    },
    "2": {
        "pregunta": "¿Te han empujado durante una discusión o al intentar retirarte?",
        "hipotesis": [("violencia_fisica", 0.60), ("violencia_psicologica", 0.30)]
    },
    "3": {
        "pregunta": "¿Has recibido jalones, bofetadas o golpes durante un conflicto?",
        "hipotesis": [("violencia_fisica", 0.80), ("violencia_psicologica", 0.40)]
    },
    "4": {
        "pregunta": "¿Te han sujetado con fuerza para impedir que te muevas o te alejes?",
        "hipotesis": [("violencia_fisica", 0.70), ("violencia_psicologica", 0.35)]
    },
    "5": {
        "pregunta": "¿Te impiden salir de un lugar cuando quieres irte?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "6": {
        "pregunta": "¿Te han aventado o empujado contra una pared o un mueble?",
        "hipotesis": [("violencia_fisica", 0.50)]
    },
    "7": {
        "pregunta": "¿Te han jalado del cabello o de la ropa para detenerte?",
        "hipotesis": [("violencia_fisica", 0.40), ("violencia_psicologica", 0.20)                                                   ]
    },
    "8": {
        "pregunta": "¿Te han aventado objetos cerca o hacia ti para intimidarte?",
        "hipotesis": [("violencia_fisica", 0.30), ("violencia_psicologica", 0.15)]
    },
    "9": {
        "pregunta": "¿Presentas marcas de dedos, sujetones o agarres en brazos o muñecas?",
        "hipotesis": [("violencia_fisica", 0.25), ("violencia_psicologica", 0.10)]
    },
    "10": {
        "pregunta": "¿Sientes dolor físico después de una discusión o enfrentamiento?",
        "hipotesis": [("violencia_fisica", 0.60), ("violencia_psicologica", 0.30)]
    },
    "11": {
        "pregunta": "¿Te has lesionado varias veces en contextos parecidos sin una explicación convincente?",
        "hipotesis": [("violencia_fisica", 0.80), ("violencia_psicologica", 0.40)]
    },
    "12": {
        "pregunta": "¿Alguien te ha inmovilizado o impedido moverte durante un conflicto?",
        "hipotesis": [("violencia_fisica", 0.70), ("violencia_psicologica", 0.35)]
    },
    "13": {
        "pregunta": "¿Golpean paredes, puertas u objetos cerca de ti para asustarte?",
        "hipotesis": [("violencia_fisica", 0.50), ("violencia_psicologica", 0.25)]
    },
    "14": {
        "pregunta": "¿Te cierran el paso o te rodean para presionarte físicamente?",
        "hipotesis": [("violencia_fisica", 0.40), ("violencia_psicologica", 0.20)]
    },
    "15": {
        "pregunta": "¿Te empujan o apartan cuando intentas hablar o defenderte?",
        "hipotesis": [("violencia_fisica", 0.30), ("violencia_psicologica", 0.15)]
    },
    "16": {
        "pregunta": "¿Te queda dolor en muñecas, brazos o cuello por cómo te sujetaron?",
        "hipotesis": [("violencia_fisica", 0.25), ("violencia_psicologica", 0.10)]
    },
    "17": {
        "pregunta": "¿Te han tirado al suelo durante una pelea o discusión?",
        "hipotesis": [("violencia_fisica", 0.60), ("violencia_psicologica", 0.30)]
    },
    "18": {
        "pregunta": "¿Usan objetos de casa para amenazarte o golpearte?",
        "hipotesis": [("violencia_fisica", 0.50), ("violencia_psicologica", 0.25)]
    },
    "19": {
        "pregunta": "¿Te impiden buscar atención médica después de una agresión?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "20": {
        "pregunta": "¿Te han sacudido o zamarreado durante una discusión?",
        "hipotesis": [("violencia_fisica", 0.40), ("violencia_psicologica", 0.20)]
    },
    "21": {
        "pregunta": "¿Notas dolor o molestia corporal frecuente después de convivir con esa persona?",
        "hipotesis": [("violencia_fisica", 0.30), ("violencia_psicologica", 0.15)]
    },
    "22": {
        "pregunta": "¿Te hacen sentir responsable de casi todo lo malo que ocurre?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "23": {
        "pregunta": "¿Te ponen obstáculos para convivir con tus amistades o familia?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "24": {
        "pregunta": "¿Sientes que te vigilan o controlan casi todo el tiempo?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "25": {
        "pregunta": "¿Minimizan o invalidan lo que sientes cuando expresas una molestia?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "26": {
        "pregunta": "¿Te amenazan con dejarte solo, sacarte de la casa o retirarte apoyo?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "27": {
        "pregunta": "¿Cambian la versión de los hechos para confundirte o hacerte dudar?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "28": {
        "pregunta": "¿Usan el silencio prolongado como castigo cuando haces algo que no les gusta?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "29": {
        "pregunta": "¿Te humillan o ridiculizan cuando están solos contigo?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "30": {
        "pregunta": "¿Te dicen que recuerdas mal aunque estés seguro de lo ocurrido?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "31": {
        "pregunta": "¿Usan los celos para controlar con quién hablas o dónde vas?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "32": {
        "pregunta": "¿Sientes que debes pedir permiso para acciones básicas de tu vida?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "33": {
        "pregunta": "¿Te dicen que tú provocas su enojo o su maltrato?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "34": {
        "pregunta": "¿Te sientes inseguro o en alerta dentro de tu casa o espacio cercano?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "35": {
        "pregunta": "¿Te comparan con otras personas para hacerte sentir menos?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "36": {
        "pregunta": "¿Te amenazan con divulgar información personal para presionarte?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "37": {
        "pregunta": "¿Te quitan libertad para decidir sobre estudios, trabajo o actividades?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "38": {
        "pregunta": "¿Te dicen que nadie te va a creer si cuentas lo que pasa?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "39": {
        "pregunta": "¿Observan cada reacción tuya para corregirte o intimidarte?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "40": {
        "pregunta": "¿Sientes que te dejan sin apoyo emocional de forma intencional?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "41": {
        "pregunta": "¿Te dicen que exageras o inventas cuando cuentas un problema?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "42": {
        "pregunta": "¿Usan el miedo o la presión para que obedezcas sin cuestionar?",
        "hipotesis": [("violencia_psicologica", 0.60)   ]
    },
    "43": {
        "pregunta": "¿Te insultan de manera directa cuando se enojan contigo?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "44": {
        "pregunta": "¿Te hablan a gritos de forma repetida o para intimidarte?",
        "hipotesis": [("violencia_psicologica", 0.50)   ]
    },
    "45": {
        "pregunta": "¿Te ponen apodos ofensivos o degradantes?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "46": {
        "pregunta": "¿Se burlan de tus errores para hacerte sentir mal?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "47": {
        "pregunta": "¿Te descalifican o te hablan como si no valieras?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "48": {
        "pregunta": "¿Te humillan delante de otras personas?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "49": {
        "pregunta": "¿Te amenazan con hacerte daño, echarte o castigarte?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "50": {
        "pregunta": "¿Usan palabras degradantes para referirse a ti?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "51": {
        "pregunta": "¿Usan sarcasmo o burlas que te dejan en ridículo?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "52": {
        "pregunta": "¿Te interrumpen o no te dejan terminar de hablar?",
        "hipotesis": [("violencia_psicologica", 0.50)]
    },
    "53": {
        "pregunta": "¿Te corrigen de manera humillante o con desprecio?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "54": {
        "pregunta": "¿Se burlan de ti cuando expresas tristeza, enojo o miedo?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "55": {
        "pregunta": "¿Te dicen cosas como que no sirves, no puedes o no vales?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "56": {
        "pregunta": "¿Te gritan delante de familiares o personas cercanas?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "57": {
        "pregunta": "¿Desacreditan tu opinión o tus logros de manera repetida?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "58": {
        "pregunta": "¿Te mandan mensajes ofensivos o insultantes?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "59": {
        "pregunta": "¿Te callan con palabras agresivas cuando intentas hablar?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "60": {
        "pregunta": "¿Se burlan de ti cuando lloras o muestras vulnerabilidad?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "61": {
        "pregunta": "¿Te culpan usando insultos o palabras ofensivas?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "62": {
        "pregunta": "¿Te dicen que te van a echar o dejar fuera usando gritos o insultos?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "63": {
        "pregunta": "¿Te hacen comentarios ofensivos sobre tu vida, decisiones o forma de ser?",
        "hipotesis": [("violencia_psicologica", 0.60)]
    },
    "64": {
        "pregunta": "¿Controlan o retienen el dinero que ganas?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "65": {
        "pregunta": "¿Te quitan la tarjeta, clave o acceso a tu dinero?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "66": {
        "pregunta": "¿Te exigen justificar cada gasto que haces?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "67": {
        "pregunta": "¿Te ponen obstáculos para que trabajes o busques empleo?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "68": {
        "pregunta": "¿Te obligan a pedir dinero para cosas básicas?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "69": {
        "pregunta": "¿Ocultan o restringen dinero para castigarte o controlarte?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "70": {
        "pregunta": "¿Usan tu nombre o te meten en deudas sin tu autorización?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "71": {
        "pregunta": "¿Hacen compras o contratos con tu nombre sin consultarte?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "72": {
        "pregunta": "¿Te quitan documentos importantes para limitarte?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "73": {
        "pregunta": "¿Te impiden pagar o usar transporte para tus actividades?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "74": {
        "pregunta": "¿Te niegan dinero para comida, medicinas o necesidades básicas?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "75": {
        "pregunta": "¿Te exigen entregar todo tu ingreso o beca?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "76": {
        "pregunta": "¿Retrasan a propósito el dinero que te corresponde para controlarte?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "77": {
        "pregunta": "¿Usan el dinero para impedir que sigas estudiando o capacitándote?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "78": {
        "pregunta": "¿Te hacen cubrir gastos que no te corresponden?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "79": {
        "pregunta": "¿Te condicionan comida, apoyo o recursos a obedecer?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "80": {
        "pregunta": "¿Retienen beca, pensión o ayuda económica que te corresponde?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "81": {
        "pregunta": "¿Te revisan y cuestionan constantemente cada compra?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "82": {
        "pregunta": "¿Cortan internet, luz, comida u otros servicios para presionarte?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "83": {
        "pregunta": "¿Te presionan para que renuncies o dejes tu empleo?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "84": {
        "pregunta": "¿Sientes que te mantienen sin recursos para que dependas de ellos?",
        "hipotesis": [("violencia_economica", 0.60)]
    },
    "85": {
        "pregunta": "¿Te tocan partes íntimas sin tu consentimiento?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "86": {
        "pregunta": "¿Te presionan para besos, abrazos o contacto físico que no quieres?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "87": {
        "pregunta": "¿Insisten en conductas sexuales después de que dijiste que no?",
        "hipotesis": [("violencia_sexual", 0.60)    ]
    },
    "88": {
        "pregunta": "¿Te hacen comentarios sexuales que te incomodan o te avergüenzan?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "89": {
        "pregunta": "¿Te presionan para enviar imágenes íntimas o privadas?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "90": {
        "pregunta": "¿Comparten fotos o videos íntimos sin tu autorización?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "91": {
        "pregunta": "¿Te tocan de forma invasiva aunque hayas pedido que paren?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "92": {
        "pregunta": "¿Te obligan a ver contenido sexual o situaciones que no deseas?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "93": {
        "pregunta": "¿Te amenazan o presionan para conseguir favores de tipo sexual?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "94": {
        "pregunta": "¿Ignoran tus límites físicos incluso cuando los expresas claramente?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "95": {
        "pregunta": "¿Reaccionan con enojo o castigo cuando rechazas algo sexual?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "96": {
        "pregunta": "¿Te hacen preguntas sexuales que te incomodan o invaden tu privacidad?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "97": {
        "pregunta": "¿Te manipulan para aceptar contacto físico o sexual?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "98": {
        "pregunta": "¿Te hacen quedarte en una situación íntima o incómoda aunque quieras salir?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "99": {
        "pregunta": "¿Revisan tu cuerpo o tu ropa sin que tú lo autorices?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "100": {
        "pregunta": "¿Hacen chistes sexuales repetidos que te incomodan?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "101": {
        "pregunta": "¿Toman fotos o videos de ti sin pedir autorización?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "102": {
        "pregunta": "¿Usan regalos, dinero o favores para presionarte sexualmente?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "103": {
        "pregunta": "¿Te dejan de hablar, te castigan o te presionan cuando marcas límites?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "104": {
        "pregunta": "¿Te han tocado de forma íntima cuando estabas dormido/a o descansando?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "105": {
        "pregunta": "¿Usan comentarios sobre tu cuerpo para presionarte o incomodarte?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "106": {
        "pregunta": "¿Te piden contraseñas o códigos de acceso para revisar tus cuentas?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "107": {
        "pregunta": "¿Revisan tu celular, chats o fotos sin tu permiso?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "108": {
        "pregunta": "¿Exigen saber dónde estás en tiempo real o revisan tu ubicación constantemente?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "109": {
        "pregunta": "¿Te exigen responder mensajes o llamadas de inmediato siempre?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "110": {
        "pregunta": "¿Crean cuentas falsas para vigilarte, seguirte o provocarte?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "111": {
        "pregunta": "¿Publican información, fotos o estados tuyos sin pedirte permiso?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "112": {
        "pregunta": "¿Comparten fotos o conversaciones privadas sin autorización?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "113": {
        "pregunta": "¿Te mandan mensajes ofensivos, burlones o amenazantes?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "114": {
        "pregunta": "¿Te amenazan, hostigan o exhiben en redes sociales?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "115": {
        "pregunta": "¿Te obligan a enseñar chats, llamadas o redes para comprobar algo?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "116": {
        "pregunta": "¿Te cambian claves o te bloquean el acceso a cuentas sin avisarte?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "117": {
        "pregunta": "¿Usan aplicaciones o herramientas para rastrear tu movimiento?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "118": {
        "pregunta": "¿Te llaman por video para comprobar dónde estás o con quién estás?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "119": {
        "pregunta": "¿Revisan con quién interactúas en redes para controlarte?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "120": {
        "pregunta": "¿Sientes que no tienes privacidad en tu vida digital?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "121": {
        "pregunta": "¿Usan tus claves para entrar a tus cuentas sin tu permiso?",
        "hipotesis": [("violencia_sexual", 0.60)    ]
    },
    "122": {
        "pregunta": "¿Difunden rumores o mensajes falsos sobre ti por internet?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "123": {
        "pregunta": "¿Te etiquetan o mencionan en publicaciones sin tu autorización?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "124": {
        "pregunta": "¿Te exigen enviar tu ubicación cada vez que sales?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "125": {
        "pregunta": "¿Borran contactos, chats o historial para aislarte o controlarte?",
        "hipotesis": [("violencia_sexual", 0.60)    ]
    },
    "126": {
        "pregunta": "¿Recibes mensajes repetidos para presionarte, vigilarte o molestarte?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "127": {
        "pregunta": "¿Te dejan sin comida suficiente o sin acceso regular a alimentos?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "128": {
        "pregunta": "¿No te atienden cuando estás enfermo/a o con dolor?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "129": {
        "pregunta": "¿Te dejan solo/a sin la supervisión necesaria?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "130": {
        "pregunta": "¿Olvidan o dejan de darte medicamentos que necesitas?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "131": {
        "pregunta": "¿No te llevan a consultas o revisiones médicas importantes?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "132": {
        "pregunta": "¿Te dejan sin ropa, abrigo o artículos básicos necesarios?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "133": {
        "pregunta": "¿No cubren necesidades básicas de higiene de forma repetida?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "134": {
        "pregunta": "¿No responden a emergencias cuando necesitas ayuda?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "135": {
        "pregunta": "¿Te dejan en un lugar inseguro o riesgoso sin cuidado?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "136": {
        "pregunta": "¿No respetan o no permiten un descanso adecuado cuando lo necesitas?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "137": {
        "pregunta": "¿Te niegan apoyo básico para cubrir necesidades esenciales?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "138": {
        "pregunta": "¿Te dejan esperando de manera constante sin recogerte o acompañarte cuando hace falta?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "139": {
        "pregunta": "¿Vives o pasas tiempo en condiciones insalubres que no corrigen?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "140": {
        "pregunta": "¿No te protegen cuando otra persona te agrede o te pone en riesgo?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "141": {
        "pregunta": "¿Ignoran señales claras de malestar, dolor o cansancio?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "142": {
        "pregunta": "¿No te dan transporte o apoyo para asistir a citas importantes?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "143": {
        "pregunta": "¿Dejan a menores sin la supervisión necesaria por periodos inadecuados?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "144": {
        "pregunta": "¿Te dejan sin acceso regular a agua o servicios básicos?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "145": {
        "pregunta": "¿No corrigen riesgos domésticos obvios y peligrosos?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "146": {
        "pregunta": "¿Te cargan responsabilidades de cuidado para las que no tienes capacidad o apoyo?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "147": {
        "pregunta": "¿Te ignoran por completo cuando estás en crisis o muy mal?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "148": {
        "pregunta": "¿Te impiden salir de casa y además revisan tu celular para controlarte?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "149": {
        "pregunta": "¿Te controlan el dinero y te insultan cuando pides algo básico?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
    "150": {
        "pregunta": "¿Después de una agresión no te llevan a revisión médica ni te apoyan?",
        "hipotesis": [("violencia_sexual", 0.60)]
    },
}