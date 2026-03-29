import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTareas


def main():

    root = tk.Tk()

    servicio = TareaServicio()

    app = AppTareas(root, servicio)

    root.mainloop()


if __name__ == "__main__":
    main()
