class Estudiantes:

    def __init__(self, Id, nombre, NotaFinal):
        self.Id = Id
        self.nombre = nombre    
        self.NotaFinal = NotaFinal

    def mostrarDatos(self):
        print(f"Id: {self.Id}, y nombre: {self.nombre}, {self.NotaFinal}")