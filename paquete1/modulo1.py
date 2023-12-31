class Cliente():
    def __init__(self, nombre, mail, edad, genero):
        self.nombre = nombre
        self.mail = mail
        self.edad = edad
        self.genero = genero

    def __str__(self):
        return f"Se ha creado el cliente {self.nombre}, {self.genero} de {self.edad} años"
    
    def comprar(self, producto, sucursal):
        self.producto = producto
        self.sucursal = sucursal
        return self.producto, self.sucursal
        
    def realizar_encuesta(self, puntuacion):
        self.puntuacion = puntuacion
        return self.puntuacion
    
    def actualizar_correo(self, mail):
        self.mail = mail
        return self.mail
