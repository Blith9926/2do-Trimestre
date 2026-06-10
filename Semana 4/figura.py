#calcular el area de un cuadrado y rectangulo utilizando clases en python

class figura:
    def __init__(self, calcular_area, calcular_perimetro):
        self.calcular_area = calcular_area
        self.calcular_perimetro = calcular_perimetro
        



class rectangulo(figura):
    def __init__(self, calcular_area, calcular_perimetro):
        super().__init__(calcular_area, calcular_perimetro)
#definir el area de un rectangulo
    def area_rectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        area_rectangulo = self.base * self.altura
        return area_rectangulo
#definir el perimetro de un rectangulo
    def perimetro_rectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        perimetro_rectangulo = 2 * (self.base + self.altura)
        return perimetro_rectangulo



class cuadrado(figura):
    def __init__(self, calcular_area, calcular_perimetro):
        super().__init__(calcular_area, calcular_perimetro)
        #definir el area de un cuadrado
    def area_cuadrado(self, lado):
        self.lado = lado
        area_cuadrado = self.lado * self.lado
        return area_cuadrado
        #definir el perimetro de un cuadrado
    def perimetro_cuadrado(self, lado):
        self.lado = lado
        perimetro_cuadrado = 4 * self.lado
        return perimetro_cuadrado




#crear una instancia de la clase cuadrado
cuadrado1 = cuadrado("calcular_area", "calcular_perimetro")
#calcular el area y perimetro de un cuadrado
area_cuadrado1 = cuadrado1.area_cuadrado(6)
perimetro_cuadrado1 = cuadrado1.perimetro_cuadrado(6)
print(f"El area del cuadrado es: {area_cuadrado1}")
print(f"El perimetro del cuadrado es: {perimetro_cuadrado1}")



#crear una instancia de la clase rectangulo
rectangulo1 = rectangulo("calcular_area", "calcular_perimetro") 
#calcular el area y perimetro de un rectangulo
area_rectangulo1 = rectangulo1.area_rectangulo(8, 15)
perimetro_rectangulo1 = rectangulo1.perimetro_rectangulo(8, 15)
print(f"El area del rectangulo es: {area_rectangulo1}")
print(f"El perimetro del rectangulo es: {perimetro_rectangulo1}")
