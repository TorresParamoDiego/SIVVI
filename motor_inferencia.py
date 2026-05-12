# motor_inferencia.py
# Lógica de evaluación del sistema experto.

from base_conocimiento import base_de_conocimiento

unidades_respuesta = [
    ("SIEMPRE", 1.0),
    ("FRECUENTEMENTE", 0.75),
    ("A VECES", 0.5),
    ("NO MUY FRECUENTEMENTE", 0.25),
    ("NUNCA", 0.0)
]


def combinar_cf(cf_acumulado, cf_nuevo):
    return cf_acumulado + cf_nuevo * (1 - cf_acumulado)


def evaluar_caso(respuestas_victima):
    resultados = {
        "violencia_fisica": 0.0,
        "violencia_psicologica": 0.0,
        "violencia_economica": 0.0,
        "violencia_sexual": 0.0,
        "violencia_verbal": 0.0,
        "violencia_digital": 0.0,
        "negligencia": 0.0
    }

    for id_hecho, multiplicador in respuestas_victima.items():
        hecho_db = base_de_conocimiento[id_hecho]
        for hipotesis, cf_base in hecho_db["hipotesis"]:
            cf_real = cf_base * multiplicador
            resultados[hipotesis] = combinar_cf(resultados[hipotesis], cf_real)
    return resultados


def interpretar_nivel(porcentaje):
    if porcentaje >= 0.85:
        return "Crítico"
    if porcentaje >= 0.60:
        return "Alto"
    if porcentaje >= 0.30:
        return "Medio"
    return "Bajo"


def descripcion_respuesta(valor):
    for label, score in unidades_respuesta:
        if score == valor:
            return label
    return "SIN RESPUESTA"
