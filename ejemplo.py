import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

from base_conocimiento import base_de_conocimiento
from motor_inferencia import evaluar_caso, interpretar_nivel, descripcion_respuesta, unidades_respuesta
from guardar_resultados import guardar_resultados
class EvaluadorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluación de Caso")
        self.root.configure(bg="#f3f4f8")
        self.root.state("zoomed")  # Windows
        #self.root.attributes("-fullscreen", True) # fullscreen real

        self.curp = tk.StringVar()
        self.preguntas = list(base_de_conocimiento.keys())
        self.indice = 0
        self.respuestas = {}
        self.omitidos = 0

        self.crear_estilos()
        self.crear_layout()
        self.crear_pantalla_curp()
    def crear_layout(self):
        self.header = tk.Frame(self.root, bg="#1e3a5f", height=90)
        self.header.pack(fill="x", side="top")

        self.header.pack_propagate(False)

        logo_izq = tk.Label(
            self.header,
            text="🏥 LOGO",
            bg="#1e3a5f",
            fg="white",
            font=("Segoe UI", 14, "bold")
        )
        logo_izq.pack(side="left", padx=20)

        titulo = tk.Label(
            self.header,
            text="Sistema de Evaluación de Caso",
            fg="white",
            bg="#1e3a5f",
            font=("Segoe UI", 22, "bold")
        )
        titulo.pack(side="left", expand=True)

        logo_der = tk.Label(
            self.header,
            text="🧠 LOGO",
            bg="#1e3a5f",
            fg="white",
            font=("Segoe UI", 14, "bold")
        )
        logo_der.pack(side="right", padx=20)

        self.contenido = tk.Frame(self.root, bg="#f3f4f8")
        self.contenido.pack(fill="both", expand=True)

        self.footer = tk.Frame(self.root, bg="#d9dde5", height=40)
        self.footer.pack(fill="x", side="bottom")

        self.footer.pack_propagate(False)

        footer_texto = tk.Label(
            self.footer,
            text="© 2026 Sistema Inteligente de Evaluación",
            bg="#d9dde5",
            fg="#333",
            font=("Segoe UI", 9)
        )

        footer_texto.pack(pady=10)
    def crear_estilos(self):
        estilo = ttk.Style(self.root)
        estilo.theme_use("clam")
        estilo.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)
        estilo.configure("Titulo.TLabel", font=("Segoe UI", 16, "bold"), background="#f3f4f8")
        estilo.configure("Subtitulo.TLabel", font=("Segoe UI", 11), background="#f3f4f8")
        estilo.configure("Pregunta.TLabel", font=("Segoe UI", 12), background="#f3f4f8")
        estilo.configure("Info.TLabel", font=("Segoe UI", 10), background="#f3f4f8")

    def crear_encabezado(self):
        header = tk.Frame(self.root, bg="#3b5998", height=80)
        header.pack(fill="x")
        titulo = tk.Label(header, text="Sistema de Evaluación de Caso", fg="white", bg="#3b5998",
                           font=("Segoe UI", 18, "bold"))
        titulo.pack(pady=18)

    def crear_pantalla_curp(self):
        self.limpiar_ventana()
        frame = tk.Frame(self.contenido, bg="#f3f4f8")
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        label_curp = ttk.Label(frame, text="Introduce tu CURP o identificador:", style="Subtitulo.TLabel")
        label_curp.pack(anchor="w", pady=(0, 8))

        entry_curp = ttk.Entry(frame, textvariable=self.curp, font=("Segoe UI", 11), width=40)
        entry_curp.pack(anchor="w", pady=(0, 15))
        entry_curp.focus()

        boton_iniciar = ttk.Button(frame, text="Iniciar cuestionario", command=self.iniciar_cuestionario)
        boton_iniciar.pack(anchor="w")

        nota = ttk.Label(frame, text="Los resultados se guardarán en resultados.csv junto al CURP.", style="Info.TLabel")
        nota.pack(anchor="w", pady=(15, 0))

    def limpiar_ventana(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def iniciar_cuestionario(self):
        texto_curp = self.curp.get().strip()
        if not texto_curp:
            messagebox.showwarning("CURP obligatorio", "Por favor ingresa tu CURP o identificador antes de comenzar.")
            return

        self.curp.set(texto_curp)
        self.mostrar_pregunta_actual()

    def mostrar_pregunta_actual(self):
        self.limpiar_ventana()

        if self.indice >= len(self.preguntas):
            self.mostrar_resultado_final()
            return

        pregunta_id = self.preguntas[self.indice]
        texto_pregunta = base_de_conocimiento[pregunta_id]["pregunta"]

        panel = tk.Frame(self.contenido, bg="#f3f4f8")
        panel.pack(fill="both", expand=True, padx=40, pady=30)

        titulo = ttk.Label(panel, text=f"Pregunta {self.indice+1} de {len(self.preguntas)}", style="Titulo.TLabel")
        titulo.pack(anchor="w")

        pregunta_label = ttk.Label(panel, text=texto_pregunta, style="Pregunta.TLabel", wraplength=self.root.winfo_width() - 100)
        pregunta_label.pack(anchor="w", pady=(12, 20))

        self.valor_seleccion = tk.DoubleVar(value=-1.0)
        opciones_frame = tk.Frame(panel, bg="#f3f4f8")
        opciones_frame.pack(anchor="w", pady=(0, 10))

        for texto, valor in unidades_respuesta:
            opcion = ttk.Radiobutton(opciones_frame, text=texto, variable=self.valor_seleccion, value=valor)
            opcion.pack(anchor="w", pady=4)

        botones_frame = tk.Frame(panel, bg="#f3f4f8")
        botones_frame.pack(anchor="w", pady=(20, 0))

        boton_saltar = ttk.Button(botones_frame, text="Saltar pregunta", command=self.saltar_pregunta)
        boton_saltar.pack(side="left", padx=(0, 10))

        boton_guardar = ttk.Button(botones_frame, text="Guardar respuesta", command=self.guardar_respuesta)
        boton_guardar.pack(side="left")

        estado = ttk.Label(panel, text=f"Omitidos: {self.omitidos}", style="Info.TLabel")
        estado.pack(anchor="w", pady=(20, 0))

    def guardar_respuesta(self):
        valor = self.valor_seleccion.get()
        if valor < 0:
            messagebox.showwarning("Respuesta requerida", "Selecciona una opción o utiliza 'Saltar pregunta'.")
            return

        pregunta_id = self.preguntas[self.indice]
        pregunta_texto = base_de_conocimiento[pregunta_id]["pregunta"]
        descripcion = descripcion_respuesta(valor)

        self.respuestas[pregunta_id] = {
            "pregunta": pregunta_texto,
            "respuesta": descripcion,
            "valor": float(valor),
            "omitida": False
        }
        self.indice += 1
        self.mostrar_pregunta_actual()

    def saltar_pregunta(self):
        pregunta_id = self.preguntas[self.indice]
        pregunta_texto = base_de_conocimiento[pregunta_id]["pregunta"]
        self.omitidos += 1
        self.respuestas[pregunta_id] = {
            "pregunta": pregunta_texto,
            "respuesta": "SALTADA",
            "valor": 0.0,
            "omitida": True
        }
        self.indice += 1
        self.mostrar_pregunta_actual()

    def mostrar_resultado_final(self):
        self.limpiar_ventana()

        resultados_globales = evaluar_caso({k: v["valor"] for k, v in self.respuestas.items()})
        promedio = sum(resultados_globales.values()) / len(resultados_globales)
        nivel = interpretar_nivel(promedio)

        panel = tk.Frame(self.contenido, bg="#f3f4f8")
        panel.pack(fill="both", expand=True, padx=40, pady=30)

        titulo = ttk.Label(panel, text="Resultado final", style="Titulo.TLabel")
        titulo.pack(anchor="w")

        resumen = (
            f"CURP: {self.curp.get()}\n"
            f"Porcentaje global: {promedio*100:.1f}%\n"
            f"Nivel global: {nivel}\n"
            f"Preguntas saltadas: {self.omitidos}"
        )
        resumen_label = ttk.Label(panel, text=resumen, style="Subtitulo.TLabel", justify="left")
        resumen_label.pack(anchor="w", pady=(10, 15))
        
        detalles_resultados = "\n".join([
            f"{categoria}: {valor*100:.1f}% - {interpretar_nivel(valor)}"
            for categoria, valor in resultados_globales.items()
        ])
        resultados_label = ttk.Label(
            panel,
            text=f"Resultados individuales:\n{detalles_resultados}",
            style="Info.TLabel",
            justify="left"
        )
        resultados_label.pack(anchor="w", pady=(0, 20))
        guardar_resultados(
            self.curp.get(),
            self.respuestas,
            self.omitidos,
            resultados_globales
        )
        finalizar = ttk.Button(panel, text="Cerrar", command=self.root.destroy)
        finalizar.pack(anchor="center", pady=(10, 0))

        messagebox.showinfo("Encuesta guardada", "El resultado se ha guardado en resultados.csv")


def main():
    root = tk.Tk()
    EvaluadorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
