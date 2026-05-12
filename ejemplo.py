# ==========================================
# 1. BASE DE DATOS DEL SISTEMA EXPERTO
# ==========================================
# Cada "hecho" (pregunta) tiene asociado a qué hipótesis afecta y su Certeza Base.
# Nota: Un hecho podría afectar a varias hipótesis (ej. aislamiento).

base_de_conocimiento = {
    "empujones": {
        "pregunta": "¿Sufres empujones o jalones por parte de tu pareja?",
        "hipotesis": [("violencia_fisica", 0.75)] # Peso 4 
    },
    "lesiones": {
        "pregunta": "¿Tienes lesiones visibles o dolor físico tras una discusión?",
        "hipotesis": [("violencia_fisica", 0.75)] # Peso 4 
    },
    "miedo_domicilio": {
        "pregunta": "¿Sientes temor de regresar a tu domicilio?",
        "hipotesis": [("violencia_fisica", 0.75), ("violencia_psicologica", 0.50)] # Afecta a dos 
    },
    "aislamiento_social": {
        "pregunta": "¿Tu pareja te aísla de tus amistades o familia?",
        "hipotesis": [("violencia_psicologica", 0.75)] # Peso 4 [cite: 8]
    },
    "humillacion": {
        "pregunta": "¿Sufres humillación constante o burlas sobre tu persona?",
        "hipotesis": [("violencia_psicologica", 0.75)] # Peso 4 [cite: 8]
    },
    "retencion_dinero": {
        "pregunta": "¿Se te retiene el dinero para los gastos básicos?",
        "hipotesis": [("violencia_economica", 0.75)] # Peso 4 [cite: 46]
    },
    "prohibicion_trabajar": {
        "pregunta": "¿Se te prohíbe trabajar o estudiar?",
        "hipotesis": [("violencia_economica", 0.90)] # Peso 5 [cite: 48]
    }
}

# ==========================================
# 2. MOTOR DE INFERENCIA (La Matemática)
# ==========================================

def combinar_cf(cf_acumulado, cf_nuevo):
    """
    Aplica la fórmula asintótica para combinar factores de certeza.
    CF_nuevo = CF_acumulado + CF_nuevo * (1 - CF_acumulado)
    """
    return cf_acumulado + cf_nuevo * (1 - cf_acumulado)

def evaluar_caso(respuestas_victima):
    """
    Toma las respuestas de la víctima (multiplicadores de 0.0 a 1.0)
    y calcula el riesgo por cada hipótesis.
    """
    # Inicializamos las hipótesis en 0% de certeza
    resultados = {
        "violencia_fisica": 0.0,
        "violencia_psicologica": 0.0,
        "violencia_economica": 0.0
    }
    
    print("\n--- PROCESANDO RESPUESTAS ---")
    
    for id_hecho, multiplicador in respuestas_victima.items():
        if multiplicador > 0:  # Solo procesamos si la respuesta no es "Nunca" (0)
            hecho_db = base_de_conocimiento[id_hecho]
            
            # Recorremos todas las hipótesis que este hecho impacta
            for hipotesis, cf_base in hecho_db["hipotesis"]:
                
                # 1. Calculamos el CF real = CF Base * Multiplicador de Frecuencia
                cf_real_del_hecho = cf_base * multiplicador
                
                # 2. Combinamos con el acumulado anterior
                cf_previo = resultados[hipotesis]
                cf_nuevo = combinar_cf(cf_previo, cf_real_del_hecho)
                
                # 3. Actualizamos el resultado
                resultados[hipotesis] = cf_nuevo
                print(f"Hecho '{id_hecho}' aportó {cf_real_del_hecho*100:.1f}% a {hipotesis}. Acumulado: {cf_nuevo*100:.1f}%")

    return resultados

def interpretar_nivel(porcentaje):
    if porcentaje >= 0.85: return "Crítico"
    if porcentaje >= 0.60: return "Alto"
    if porcentaje >= 0.30: return "Medio"
    return "Bajo"

# ==========================================
# 3. SIMULACIÓN DE UN CASO REAL
# ==========================================
# Escala de respuestas: 0.0 (Nunca), 0.5 (A veces), 1.0 (Frecuentemente)

print("SIMULACIÓN DE CASO: 'María'")
# María responde el cuestionario:
respuestas_maria = {
    "empujones": 1.0,           # SÍ, frecuentemente
    "lesiones": 0.0,            # NO, nunca (quizás lo oculta o no deja marcas)
    "miedo_domicilio": 0.5,     # A veces siente miedo
    "aislamiento_social": 1.0,  # SÍ, la aísla totalmente
    "humillacion": 1.0,         # SÍ, constante
    "retencion_dinero": 0.0,    # NO
    "prohibicion_trabajar": 0.0 # NO
}

# Ejecutamos el motor de inferencia
riesgos_finales = evaluar_caso(respuestas_maria)

# Mostramos el reporte final
print("\n=== REPORTE FINAL DEL SISTEMA EXPERTO ===")
for hipotesis, certeza in riesgos_finales.items():
    nivel = interpretar_nivel(certeza)
    print(f"- {hipotesis.replace('_', ' ').capitalize()}: {certeza*100:.1f}% -> Nivel: {nivel}")