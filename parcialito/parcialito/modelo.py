class Nodo:
    def __init__(self, figura):
        self.figura = figura
        self.siguiente = None
        self.anterior = None

class Modelo:
    def __init__(self):
        self.cabeza = None
        self.actual = None
        
        self.orden_figuras = ['circulo', 'triangulo', 'cuadrado']
        
        self.colores_fijos = ['red', 'green', 'blue'] 
        
        self.rotacion_ciclos = 0
        
        self._inicializar_lista_circular()
        
    def _inicializar_lista_circular(self):
        nodos = [Nodo(f) for f in self.orden_figuras]
        for i in range(len(nodos)):
            nodos[i].siguiente = nodos[(i + 1) % len(nodos)]
            nodos[i].anterior = nodos[(i - 1) % len(nodos)]

        self.cabeza = nodos[0]
        self.actual = self.cabeza 
        
    def _obtener_indice_actual(self):
        current = self.cabeza
        index = 0
        while current != self.actual:
            current = current.siguiente
            index += 1
            if current == self.cabeza: 
                break 
        return index

    def _obtener_color_rotado(self):
        indice_figura = self._obtener_indice_actual()
            
        num_colores = len(self.colores_fijos)
        indice_color = (indice_figura + self.rotacion_ciclos) % num_colores
        
        return self.colores_fijos[indice_color]


    def obtener_estado_actual(self):
        if self.actual:
            figura = self.actual.figura
            color = self._obtener_color_rotado()
            return {'figura': figura, 'color': color}
        return None

    def avanzar(self):
        if self.actual:
            
            self.actual = self.actual.siguiente
            
            if self.actual == self.cabeza:
                num_colores = len(self.colores_fijos)
                self.rotacion_ciclos = (self.rotacion_ciclos + 1) % num_colores


    def retroceder(self):
        if self.actual:
            
            if self.actual == self.cabeza:
                num_colores = len(self.colores_fijos)
                self.rotacion_ciclos = (self.rotacion_ciclos - 1 + num_colores) % num_colores
            
            self.actual = self.actual.anterior