class Cliente():
    def __init__(self, nombre, mail, edad, genero):
        self.nombre = nombre
        self.mail = mail
        self.edad = edad
        self.genero = genero

    def __str__(self):
        return f"Se ha creado el cliente {self.nombre}, {self.genero} de {self.edad} años"
    
    def comprar(self, producto, lugar):
        self.producto = producto
        self.lugar = lugar
        print (f"El cliente ha comprado {self.producto} en {self.lugar}")
    
    def actualizardireccion(self, nombrecalle, numerocalle):
        self.nombrecalle = nombrecalle
        self.numerocalle = numerocalle
        print (f"Se ha actualizado la direccion a {nombrecalle} {numerocalle}")
        
    
