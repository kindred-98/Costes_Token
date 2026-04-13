"""Interfaz de escritorio para Calculadora de Costes."""

import tkinter as tk
from tkinter import ttk, messagebox
from src import CalculadoraCostes, ProyeccionMensual, estimar_tokens

import customtkinter as ctk

# ─── CONFIGURACIÓN GLOBAL DE TEMA (va ANTES de crear la ventana) ───
ctk.set_appearance_mode("dark")          # fondo oscuro #2b2b2b
ctk.set_default_color_theme("dark-blue") # acento azul en widgets

class CalculadoraApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Costes de APIs de IA")
        self.geometry("420x580")
        self.resizable(False, False)
        self._construir_gui()

    def _construir_gui(self):
        PAD = {"padx": 20, "pady": (0, 10)}

        # ── Etiqueta + Entry: Modelo de IA ──
        ctk.CTkLabel(self, text="Modelo de IA", anchor="w").pack(
            fill="x", padx=20, pady=(20, 4)
        )
        self.entry_modelo = ctk.CTkEntry(self, placeholder_text="gpt-4o")
        self.entry_modelo.pack(fill="x", **PAD)
        self.entry_modelo.insert(0, "gpt-4o")

        # ── Etiqueta + Textbox: Texto a analizar ──
        ctk.CTkLabel(self, text="Texto a analizar", anchor="w").pack(
            fill="x", padx=20, pady=(10, 4)
        )
        self.texto_entrada = ctk.CTkTextbox(self, height=80)
        self.texto_entrada.pack(fill="x", **PAD)

        # ── Fila de botones ──
        fila_botones = ctk.CTkFrame(self, fg_color="transparent")
        fila_botones.pack(fill="x", padx=20, pady=(6, 16))

        ctk.CTkButton(
            fila_botones, text="Calcular Costes",
            fg_color="#1a1a1a",          # negro apagado
            hover_color="#333",
            command=self._calcular
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            fila_botones, text="Limpiar",
            fg_color="#3a3a3a",          # gris medio
            hover_color="#555",
            command=self._limpiar
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            fila_botones, text="Salir",
            fg_color="#c0392b",          # rojo igual que la imagen
            hover_color="#e74c3c",
            command=self.destroy
        ).pack(side="left")

        # ── Título Resultados ──
        ctk.CTkLabel(
            self, text="Resultados",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#4fc3f7",        # azul claro
            anchor="w"
        ).pack(fill="x", padx=20, pady=(0, 8))

        # ── Tarjeta Tokens (fondo verde oscuro) ──
        self.frame_tokens = ctk.CTkFrame(
            self, fg_color="#2d3d2d", corner_radius=8
        )
        self.frame_tokens.pack(fill="x", padx=20, pady=(0, 10))

        ctk.CTkLabel(
            self.frame_tokens, text="● Tokens",
            text_color="#81c784", anchor="w",
            font=ctk.CTkFont(weight="bold")
        ).pack(fill="x", padx=12, pady=(8, 2))

        self.lbl_entrada  = ctk.CTkLabel(self.frame_tokens, text="⬆  Entrada: —", anchor="w", text_color="#aaa")
        self.lbl_salida   = ctk.CTkLabel(self.frame_tokens, text="⬇  Salida (estimada): —", anchor="w", text_color="#aaa")
        self.lbl_total_tk = ctk.CTkLabel(self.frame_tokens, text="⬇  Total: —", anchor="w", text_color="#aaa")
        for lbl in (self.lbl_entrada, self.lbl_salida, self.lbl_total_tk):
            lbl.pack(fill="x", padx=12, pady=1)
        ctk.CTkLabel(self.frame_tokens, text="").pack(pady=2)  # spacer

        # ── Tarjeta Costes (fondo ámbar oscuro) ──
        self.frame_costes = ctk.CTkFrame(
            self, fg_color="#3d2d1a", corner_radius=8
        )
        self.frame_costes.pack(fill="x", padx=20, pady=(0, 16))

        ctk.CTkLabel(
            self.frame_costes, text="● Costes",
            text_color="#ffb74d", anchor="w",
            font=ctk.CTkFont(weight="bold")
        ).pack(fill="x", padx=12, pady=(8, 2))

        self.lbl_euros    = ctk.CTkLabel(self.frame_costes, text="💶  Euros:      —", anchor="w", text_color="#aaa")
        self.lbl_dolares  = ctk.CTkLabel(self.frame_costes, text="💵  Dólar:      —", anchor="w", text_color="#aaa")
        self.lbl_centimos = ctk.CTkLabel(self.frame_costes, text="¢   Céntimos:  —", anchor="w", text_color="#aaa")
        for lbl in (self.lbl_euros, self.lbl_dolares, self.lbl_centimos):
            lbl.pack(fill="x", padx=12, pady=1)
        ctk.CTkLabel(self.frame_costes, text="").pack(pady=2)

    def _calcular(self):
        modelo = self.entry_modelo.get().strip() or "gpt-4o"
        texto = self.texto_entrada.get("1.0", "end").strip()
        
        if not texto:
            return
        
        try:
            tokens_entrada = estimar_tokens(texto, modelo)
        except:
            tokens_entrada = max(1, len(texto.split()))
        
        tokens_salida = 200
        total = tokens_entrada + tokens_salida

        try:
            calc = CalculadoraCostes(modelo)
            coste = calc.calcular_costes(tokens_entrada, tokens_salida)
            costo_usd = coste.coste_total_usd
        except:
            precio_entrada_usd = 0.000005
            precio_salida_usd = 0.000015
            costo_usd = tokens_entrada * precio_entrada_usd + tokens_salida * precio_salida_usd

        costo_eur = costo_usd * 0.92
        costo_cts = costo_eur * 100

        self.lbl_entrada.configure(text=f"⬆  Entrada: {tokens_entrada} tokens")
        self.lbl_salida.configure(text=f"⬇  Salida (estimada): {tokens_salida} tokens")
        self.lbl_total_tk.configure(text=f"▣  Total: {total} tokens")
        self.lbl_euros.configure(text=f"💶  Euros:      {costo_eur:.6f} €")
        self.lbl_dolares.configure(text=f"💵  Dólar:      {costo_usd:.6f} $")
        self.lbl_centimos.configure(text=f"¢   Céntimos:  {costo_cts:.4f} cts")

    def _limpiar(self):
        self.texto_entrada.delete("1.0", "end")
        for lbl in (self.lbl_entrada, self.lbl_salida, self.lbl_total_tk,
                    self.lbl_euros, self.lbl_dolares, self.lbl_centimos):
            texto_original = lbl.cget("text").split(":")[0]
            lbl.configure(text=f"{texto_original}: —")


if __name__ == "__main__":
    app = CalculadoraApp()
    app.mainloop()