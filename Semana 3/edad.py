from datetime import datetime

class Usuario:

    def __init__(self, cedula, nombre, anoNacimiento, mesNacimiento, diaNacimiento):
        self.cedula = cedula
        self.nombre = nombre
        self.anoNacimiento = anoNacimiento
        self.mesNacimiento = mesNacimiento
        self.diaNacimiento = diaNacimiento

    def mostrarDatos(self):
        fechaNacimiento = datetime(self.anoNacimiento, self.mesNacimiento, self.diaNacimiento)
        
        hoy = datetime.now()
        edad = hoy.year - fechaNacimiento.year
        if( hoy.month, hoy.day ) < (fechaNacimiento.month, fechaNacimiento.day):
            edad -= 1
        
        print(f"Cedula: {self.cedula}, nombre: {self.nombre} y edad: {edad}")