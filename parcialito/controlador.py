class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def actualizar_vista(self):
        estado = self.modelo.obtener_estado_actual()
        if estado:
            self.vista.mostrar_figura(estado['figura'], estado['color'])

    def mostrar_siguiente(self):
        self.modelo.avanzar()
        self.actualizar_vista()

    def mostrar_anterior(self):
        self.modelo.retroceder()
        self.actualizar_vista()
