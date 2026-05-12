# guardar_resultados.py
# Funciones para persistir resultados en un archivo CSV.

import csv
import os
from datetime import datetime

RESULTADOS_FILE = "resultados.csv"


def guardar_resultados(curp, respuestas, omitidos, resultados_globales):
    existe = os.path.exists(RESULTADOS_FILE)
    with open(RESULTADOS_FILE, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        if not existe:
            escritor.writerow([
                "timestamp",
                "curp",
                "pregunta_id",
                "pregunta",
                "respuesta",
                "valor",
                "omitida",
                "omitted_count",
                "violencia_fisica",
                "violencia_psicologica",
                "violencia_economica",
                "violencia_sexual",
                "violencia_verbal",
                "violencia_digital",
                "negligencia"
            ])

        timestamp = datetime.now().isoformat(timespec="seconds")
        viol_fisica = resultados_globales.get("violencia_fisica", 0.0)
        viol_psico = resultados_globales.get("violencia_psicologica", 0.0)
        viol_econ = resultados_globales.get("violencia_economica", 0.0)
        viol_sex = resultados_globales.get("violencia_sexual", 0.0)
        viol_ver = resultados_globales.get("violencia_verbal", 0.0)
        viol_dig = resultados_globales.get("violencia_digital", 0.0)
        negligencia = resultados_globales.get("negligencia", 0.0)

        for pregunta_id, datos in respuestas.items():
            escritor.writerow([
                timestamp,
                curp,
                pregunta_id,
                datos.get("pregunta", ""),
                datos.get("respuesta", ""),
                datos.get("valor", 0.0),
                datos.get("omitida", False),
                omitidos,
                f"{viol_fisica:.4f}",
                f"{viol_psico:.4f}",
                f"{viol_econ:.4f}",
                f"{viol_sex:.4f}",
                f"{viol_ver:.4f}",
                f"{viol_dig:.4f}",
                f"{negligencia:.4f}"
            ])
