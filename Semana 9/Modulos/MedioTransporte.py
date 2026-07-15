class IntrumentosMusicales:
    def __init__(self, material, marca, modelo, anno):
        self.material = material
        self.marca = marca
        self.modelo = modelo
        self.anno = anno

    def hacer_sonido(self):
        print("Hacer sonido de instrumento")

class IntrumentosMusicalesViento(IntrumentosMusicales):
    def __init__(self, material, marca, modelo, anno):
        super().__init__(material, marca, modelo, anno)

    def hacer_sonido(self): #Polimorfismo
        print("Sonido de viento")

class IntrumentosMusicalesCuerdas(IntrumentosMusicales): #Herencia
    def __init__(self, material, marca, modelo, anno, cantidadCuerdas):
        self.cantidadCuerdas = cantidadCuerdas
        super().__init__(material, marca, modelo, anno)

    def hacer_sonido(self):
        print("Sonido de cuerdas")

guitarrra = IntrumentosMusicalesCuerdas("madera", "yamaha", "acustico", 2026, 6)
guitarrra.hacer_sonido()

traversi = IntrumentosMusicalesViento("plastico", "yamaha", "acustico", 2026)
traversi.hacer_sonido()