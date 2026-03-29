import tkinter as tk
from tkinter import ttk, messagebox


class AppTareas:

    def __init__(self, root, servicio):

        self.root = root
        self.root.title("Lista de Tareas")

        self.servicio = servicio

        # ===== INPUT =====
        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=0, column=0)

        # EVENTO ENTER (IMPORTANTE)
        self.entry.bind("<Return>", self.agregar_evento)

        # ===== BOTONES =====
        tk.Button(root, text="Añadir Tarea", command=self.agregar).grid(row=0, column=1)
        tk.Button(root, text="Marcar Completada", command=self.completar).grid(row=1, column=0)
        tk.Button(root, text="Eliminar", command=self.eliminar).grid(row=1, column=1)

        # ===== LISTA =====
        self.lista = tk.Listbox(root, width=50)
        self.lista.grid(row=2, column=0, columnspan=2)

        # EVENTO DOBLE CLICK (EXTRA)
        self.lista.bind("<Double-1>", self.completar_evento)

    # ===== FUNCIONES =====

    def agregar(self):
        texto = self.entry.get()

        if texto == "":
            messagebox.showwarning("Error", "Campo vacío")
            return

        self.servicio.agregar_tarea(texto)
        self.actualizar()
        self.entry.delete(0, tk.END)

    def agregar_evento(self, event):
        self.agregar()

    def completar(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            return

        index = seleccion[0]
        tarea = self.servicio.obtener_tareas()[index]

        self.servicio.completar_tarea(tarea.id)
        self.actualizar()

    def completar_evento(self, event):
        self.completar()

    def eliminar(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            return

        index = seleccion[0]
        tarea = self.servicio.obtener_tareas()[index]

        self.servicio.eliminar_tarea(tarea.id)
        self.actualizar()

    def actualizar(self):
        self.lista.delete(0, tk.END)

        for t in self.servicio.obtener_tareas():
            texto = t.descripcion

            if t.completada:
                texto = "[Hecho] " + texto

            self.lista.insert(tk.END, texto)
