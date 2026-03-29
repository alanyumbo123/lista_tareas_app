from modelos.tarea import Tarea


class TareaServicio:

    def __init__(self):
        self._tareas = []
        self._contador = 1

    def agregar_tarea(self, descripcion):
        tarea = Tarea(self._contador, descripcion)
        self._tareas.append(tarea)
        self._contador += 1

    def obtener_tareas(self):
        return self._tareas

    def completar_tarea(self, id):
        for t in self._tareas:
            if t.id == id:
                t.completada = True

    def eliminar_tarea(self, id):
        for t in self._tareas:
            if t.id == id:
                self._tareas.remove(t)
                return
