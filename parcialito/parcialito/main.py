import tkinter as tk
from modelo import Modelo
from vista import Vista
from controlador import Controlador

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MVC - Lista Circular")

    model = Modelo()
    view = Vista(root)
    controller = Controlador(model, view)

    view.siguiente_btn.config(command=controller.mostrar_siguiente)
    view.anterior_btn.config(command=controller.mostrar_anterior)

    controller.actualizar_vista()

    root.mainloop()