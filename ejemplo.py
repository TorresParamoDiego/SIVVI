import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

from base_conocimiento import base_de_conocimiento
from motor_inferencia import evaluar_caso, interpretar_nivel, descripcion_respuesta, unidades_respuesta
from guardar_resultados import guardar_resultados


class EvaluadorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluación de Caso")
        self.root.configure(bg="#f3f4f8")

        self.centrar_ventana(1024, 768)
        self.root.minsize(800, 600)

        self.colors = {
            "bg": "#f3f4f8",
            "card": "#ffffff",
            "text": "#111827",
            "muted": "#6b7280",
            "border": "#d1d5db",
            "header": "#1e3a5f",
            "accent": "#2563eb",
            "accent_dark": "#1d4ed8"
        }

        self.curp = tk.StringVar()
        self.ubicacion = tk.StringVar()
        self.preguntas = list(base_de_conocimiento.keys())
        self.indice = 0
        self.respuestas = {}
        self.omitidos = 0
        self.tamanio_base = 11
        self.start_time = None
        self.suppress_save = False

        self.estilo = ttk.Style(self.root)
        self.estilo.theme_use("clam")

        self.crear_layout()
        self.actualizar_estilos()
        self.crear_pantalla_curp()

    def centrar_ventana(self, ancho, alto):
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        x = int((ancho_pantalla / 2) - (ancho / 2))
        y = int((alto_pantalla / 2) - (alto / 2))
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def crear_layout(self):
        self.header = tk.Frame(self.root, bg=self.colors["header"], height=80)
        self.header.pack(fill="x", side="top")
        self.header.pack_propagate(False)

        header_left = tk.Frame(self.header, bg=self.colors["header"])
        header_left.pack(side="left", padx=32, pady=12)

        self.lbl_titulo_header = tk.Label(
            header_left,
            text="Sistema de Evaluación de Caso",
            fg="white",
            bg=self.colors["header"],
            font=("Segoe UI", 18, "bold")
        )
        self.lbl_titulo_header.pack(anchor="w")

        self.lbl_sub_header = tk.Label(
            header_left,
            text="Cuestionario guiado y resultados inmediatos",
            fg="#dbeafe",
            bg=self.colors["header"],
            font=("Segoe UI", 10)
        )
        self.lbl_sub_header.pack(anchor="w")

        header_right = tk.Frame(self.header, bg=self.colors["header"])
        header_right.pack(side="right", padx=32)

        self.lbl_estado_header = tk.Label(
            header_right,
            text="Modo entrevista",
            fg="#dbeafe",
            bg=self.colors["header"],
            font=("Segoe UI", 10, "bold")
        )
        self.lbl_estado_header.pack(anchor="e")

        self.contenido = tk.Frame(self.root, bg=self.colors["bg"])
        self.contenido.pack(fill="both", expand=True)

        self.footer = tk.Frame(self.root, bg="#e5e7eb", height=45)
        self.footer.pack(fill="x", side="bottom")
        self.footer.pack_propagate(False)

        self.lbl_footer = tk.Label(
            self.footer,
            # text="© 2026 Sistema Inteligente de Evaluación",
            bg="#e5e7eb",
            fg="#374151",
            font=("Segoe UI", 9)
        )
        self.lbl_footer.pack(side="left", padx=32)

        # Control de accesibilidad (tamaño de fuente)
        control_fuente = tk.Frame(self.footer, bg="#e5e7eb")
        control_fuente.pack(side="right", padx=32)

        tk.Label(control_fuente, text="A-", bg="#e5e7eb", fg="#374151", font=("Segoe UI", 9, "bold")).pack(side="left")

        self.escala_fuente = ttk.Scale(
            control_fuente,
            from_=9, to=20,
            orient="horizontal",
            command=self.cambiar_fuente,
            length=150
        )
        self.escala_fuente.set(self.tamanio_base)
        self.escala_fuente.pack(side="left", padx=8)

        tk.Label(control_fuente, text="A+", bg="#e5e7eb", fg="#374151", font=("Segoe UI", 12, "bold")).pack(side="left")

    def cambiar_fuente(self, valor):
        self.tamanio_base = int(float(valor))
        self.actualizar_estilos()

    def actualizar_estilos(self):
        base = self.tamanio_base

        # Elementos estáticos (Header / Footer)
        self.lbl_titulo_header.config(font=("Segoe UI", base + 7, "bold"))
        self.lbl_sub_header.config(font=("Segoe UI", base - 1))
        self.lbl_estado_header.config(font=("Segoe UI", base - 1, "bold"))
        self.lbl_footer.config(font=("Segoe UI", base - 2))

        # Estilos dinámicos ttk
        self.estilo.configure("TButton", font=("Segoe UI", base, "bold"), padding=8)
        self.estilo.configure("Primary.TButton",
                              font=("Segoe UI", base, "bold"),
                              background=self.colors["accent"],
                              foreground="white",
                              padding=(16, 8))
        self.estilo.map("Primary.TButton",
                        background=[("active", self.colors["accent_dark"]), ("disabled", "#cbd5f5")],
                        foreground=[("disabled", "#f3f4f8")])

        self.estilo.configure("Secondary.TButton",
                              font=("Segoe UI", base, "bold"),
                              background="#e5e7eb",
                              foreground="#111827",
                              padding=(14, 8))
        self.estilo.map("Secondary.TButton", background=[("active", "#d1d5db")])

        self.estilo.configure("Titulo.TLabel", font=("Segoe UI", base + 7, "bold"), background=self.colors["card"],
                              foreground=self.colors["text"])
        self.estilo.configure("Subtitulo.TLabel", font=("Segoe UI", base), background=self.colors["card"],
                              foreground=self.colors["text"])
        self.estilo.configure("Pregunta.TLabel", font=("Segoe UI", base + 3), background=self.colors["card"],
                              foreground=self.colors["text"])
        self.estilo.configure("Info.TLabel", font=("Segoe UI", base - 1), background=self.colors["card"],
                              foreground=self.colors["muted"])
        self.estilo.configure("Muted.TLabel", font=("Segoe UI", base - 2), background=self.colors["card"],
                              foreground=self.colors["muted"])
        self.estilo.configure("Card.TFrame", background=self.colors["card"])
        self.estilo.configure("TRadiobutton", background=self.colors["card"], font=("Segoe UI", base))
        self.estilo.configure("TEntry", padding=8, font=("Segoe UI", base + 1))
        self.estilo.configure("TProgressbar", thickness=10)

    def crear_tarjeta(self):
        tarjeta_borde = tk.Frame(
            self.contenido,
            bg=self.colors["border"],
            padx=1, pady=1
        )
        tarjeta_borde.pack(expand=True)

        tarjeta = tk.Frame(
            tarjeta_borde,
            bg=self.colors["card"],
            padx=48, pady=40
        )
        tarjeta.pack(fill="both", expand=True)
        return tarjeta

    def crear_pantalla_curp(self):
        self.limpiar_ventana()
        self.root.unbind("<Return>")

        tarjeta = self.crear_tarjeta()

        titulo = ttk.Label(tarjeta, text="Bienvenida", style="Titulo.TLabel")
        titulo.pack(anchor="w", pady=(0, 8))

        texto = ttk.Label(
            tarjeta,
            text="Ingresa el CURP o identificador del caso para comenzar la entrevista.",
            style="Subtitulo.TLabel"
        )
        texto.pack(anchor="w", pady=(0, 24))

        label_curp = ttk.Label(tarjeta, text="CURP o ID", style="Muted.TLabel")
        label_curp.pack(anchor="w", pady=(0, 6))

        entry_curp = ttk.Entry(tarjeta, textvariable=self.curp, width=35, style="TEntry")
        entry_curp.pack(anchor="w", pady=(0, 12))
        entry_curp.focus()

        label_ubic = ttk.Label(tarjeta, text="Ubicación (lugar donde se realiza)", style="Muted.TLabel")
        label_ubic.pack(anchor="w", pady=(0, 6))

        entry_ubic = ttk.Entry(tarjeta, textvariable=self.ubicacion, width=35, style="TEntry")
        entry_ubic.pack(anchor="w", pady=(0, 12))

        ayuda = ttk.Label(
            tarjeta,
            text="Usa mayúsculas y sin espacios. Los resultados se guardarán automáticamente.",
            style="Info.TLabel"
        )
        ayuda.pack(anchor="w", pady=(0, 24))

        boton_iniciar = ttk.Button(tarjeta, text="Iniciar cuestionario", style="Primary.TButton",
                                   command=self.iniciar_cuestionario)
        boton_iniciar.pack(anchor="w")

        self.root.bind("<Return>", lambda event: self.iniciar_cuestionario())

    def limpiar_ventana(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def iniciar_cuestionario(self):
        texto_curp = self.curp.get().strip()
        if not texto_curp:
            messagebox.showwarning("Dato obligatorio", "Por favor ingresa un CURP o identificador válido.")
            return

        self.curp.set(texto_curp)
        self.indice = 0
        self.respuestas = {}
        self.omitidos = 0
        self.start_time = datetime.now()
        self.suppress_save = False
        self.mostrar_pregunta_actual()

    def mostrar_pregunta_actual(self):
        self.limpiar_ventana()
        if self.indice >= len(self.preguntas):
            self.mostrar_resultado_final()
            return

        pregunta_id = self.preguntas[self.indice]
        texto_pregunta = base_de_conocimiento[pregunta_id]["pregunta"]

        tarjeta = self.crear_tarjeta()

        progreso_frame = tk.Frame(tarjeta, bg=self.colors["card"])
        progreso_frame.pack(fill="x", pady=(0, 20))

        progreso_label = ttk.Label(
            progreso_frame,
            text=f"Pregunta {self.indice + 1} de {len(self.preguntas)}",
            style="Muted.TLabel"
        )
        progreso_label.pack(anchor="w", pady=(0, 6))

        progreso = ttk.Progressbar(
            progreso_frame,
            value=self.indice + 1,
            maximum=len(self.preguntas)
        )
        progreso.pack(fill="x")

        pregunta_label = ttk.Label(
            tarjeta,
            text=texto_pregunta,
            style="Pregunta.TLabel",
            wraplength=700
        )
        pregunta_label.pack(anchor="w", pady=(0, 24))

        self.valor_seleccion = tk.DoubleVar(value=-1.0)
        opciones_frame = tk.Frame(tarjeta, bg=self.colors["card"])
        opciones_frame.pack(anchor="w", pady=(0, 24))

        # Si ya existe una respuesta previa, precargarla
        prev = self.respuestas.get(pregunta_id)
        if prev and not prev.get("omitida", False):
            try:
                self.valor_seleccion.set(float(prev.get("valor", -1.0)))
            except Exception:
                self.valor_seleccion.set(-1.0)

        for texto, valor in unidades_respuesta:
            opcion = ttk.Radiobutton(opciones_frame, text=texto, variable=self.valor_seleccion, value=valor,
                                     command=lambda v=valor: self._on_option_selected(v))
            opcion.pack(anchor="w", pady=6)

        botones_frame = tk.Frame(tarjeta, bg=self.colors["card"])
        botones_frame.pack(fill="x", pady=(0, 8))

        boton_regresar = ttk.Button(botones_frame, text="Regresar", style="Secondary.TButton",
                                    command=self.regresar_pregunta)
        boton_regresar.pack(side="left")

        boton_saltar = ttk.Button(botones_frame, text="Saltar pregunta", style="Secondary.TButton",
                                  command=self.saltar_pregunta)
        boton_saltar.pack(side="left", padx=(12, 0))

        estado = ttk.Label(tarjeta, text=f"Omitidas: {self.omitidos}", style="Info.TLabel")
        estado.pack(anchor="e")

        # Enter key: confirmar opción seleccionada si hay una
        self.root.bind("<Return>", lambda event: self._enter_pressed())

    def _actualizar_boton_guardar(self, *_):
        # ya no se usa: guardado automático al seleccionar
        pass

    def _on_option_selected(self, valor):
        if getattr(self, "suppress_save", False):
            return
        # Guardar inmediatamente y pasar a la siguiente pregunta
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

    def _enter_pressed(self):
        v = self.valor_seleccion.get()
        if v >= 0:
            self._on_option_selected(v)
        else:
            messagebox.showwarning("Respuesta requerida", "Selecciona una opción o utiliza 'Saltar pregunta'.")

    def guardar_respuesta(self):
        # preservado por compatibilidad; ahora el guardado es automático al seleccionar
        v = self.valor_seleccion.get()
        if v >= 0:
            self._on_option_selected(v)

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

    def regresar_pregunta(self):
        if self.indice <= 0:
            # volver a la pantalla inicial
            self.crear_pantalla_curp()
            return
        self.indice -= 1
        # Al mostrar la pregunta anterior, la respuesta previa (si existe) se precargará
        self.mostrar_pregunta_actual()

    def mostrar_resultado_final(self):
        self.limpiar_ventana()
        self.root.unbind("<Return>")

        resultados_globales = evaluar_caso({k: v["valor"] for k, v in self.respuestas.items()})
        promedio = sum(resultados_globales.values()) / len(resultados_globales)
        nivel = interpretar_nivel(promedio)

        total_time_seconds = None
        if self.start_time:
            total_time_seconds = (datetime.now() - self.start_time).total_seconds()

        tarjeta = self.crear_tarjeta()

        titulo = ttk.Label(tarjeta, text="Resultado Final de Evaluación", style="Titulo.TLabel")
        titulo.pack(anchor="w", pady=(0, 16))

        resumen = (
            f"CURP / ID: {self.curp.get()}\n"
            f"Porcentaje global: {promedio * 100:.1f}%\n"
            f"Nivel global: {nivel}\n"
            f"Preguntas saltadas: {self.omitidos}"
        )
        resumen_label = ttk.Label(tarjeta, text=resumen, style="Subtitulo.TLabel", justify="left")
        resumen_label.pack(anchor="w", pady=(0, 20))

        detalles_resultados = "\n".join([
            f"• {categoria}: {valor * 100:.1f}% - {interpretar_nivel(valor)}"
            for categoria, valor in resultados_globales.items()
        ])

        resultados_label = ttk.Label(
            tarjeta,
            text=f"Desglose por categorías:\n\n{detalles_resultados}",
            style="Pregunta.TLabel",
            justify="left"
        )
        resultados_label.pack(anchor="w", pady=(0, 24))

        guardar_resultados(
            self.curp.get(),
            self.respuestas,
            self.omitidos,
            resultados_globales,
            total_time_seconds=total_time_seconds,
            ubicacion=self.ubicacion.get()
        )

        botones_frame = tk.Frame(tarjeta, bg=self.colors["card"])
        botones_frame.pack(anchor="w", pady=(12, 0))

        btn_repetir = ttk.Button(botones_frame, text="Nueva Evaluación", style="Secondary.TButton",
                                 command=self.reiniciar_sistema)
        btn_repetir.pack(side="left", padx=(0, 12))

        finalizar = ttk.Button(botones_frame, text="Cerrar Sistema", style="Primary.TButton", command=self.root.destroy)
        finalizar.pack(side="left")

    def reiniciar_sistema(self):
        self.curp.set("")
        self.indice = 0
        self.respuestas.clear()
        self.omitidos = 0
        self.crear_pantalla_curp()


def main():
    root = tk.Tk()
    EvaluadorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
