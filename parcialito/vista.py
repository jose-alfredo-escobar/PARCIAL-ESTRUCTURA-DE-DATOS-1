import tkinter as tk

class Vista:
    def __init__(self, master):
        self.master = master
        
        self.canvas = tk.Canvas(master, width=300, height=300, bg='white')
        self.canvas.pack(pady=10)
        
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)
        
        self.anterior_btn = tk.Button(button_frame, text="Anterior")
        self.anterior_btn.pack(side=tk.LEFT, padx=10)
        
        self.siguiente_btn = tk.Button(button_frame, text="Siguiente")
        self.siguiente_btn.pack(side=tk.RIGHT, padx=10)
        
        self.figura_id = None 

    def mostrar_figura(self, figura, color):
        self.canvas.delete("all")
        
        center_x, center_y = 150, 150
        size = 100
        
        if figura == 'circulo':
            self.figura_id = self.canvas.create_oval(
                center_x - size/2, center_y - size/2, 
                center_x + size/2, center_y + size/2, 
                fill=color, outline='black'
            )
        elif figura == 'triangulo':
            p1 = (center_x, center_y - size/2)
            p2 = (center_x - size/2, center_y + size/2)
            p3 = (center_x + size/2, center_y + size/2)
            self.figura_id = self.canvas.create_polygon(
                p1, p2, p3, 
                fill=color, outline='black'
            )
        elif figura == 'cuadrado':
            self.figura_id = self.canvas.create_rectangle(
                center_x - size/2, center_y - size/2, 
                center_x + size/2, center_y + size/2, 
                fill=color, outline='black'
            )
