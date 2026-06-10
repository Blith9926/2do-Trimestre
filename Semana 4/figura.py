#calcular el area de un cuadrado y rectangulo utilizando clases en python

class figura:
    def __init__(self, calcular_area, calcular_perimetro):
        self.calcular_area = calcular_area
        self.calcular_perimetro = calcular_perimetro
        



class rectangulo(figura):
    def __init__(self, calcular_area, calcular_perimetro):
        super().__init__(calcular_area, calcular_perimetro)
#definir el area de un rectangulo
    def area(self, base, altura):
        self.base = base
        self.altura = altura
        area = self.base * self.altura
        return area
#definir el perimetro de un rectangulo
    def perimetro(self, base, altura):
        self.base = base
        self.altura = altura
        perimetro = 2 * (self.base + self.altura)
        return perimetro



class cuadrado(figura):
    def __init__(self, calcular_area, calcular_perimetro):
        super().__init__(calcular_area, calcular_perimetro)
        #definir el area de un cuadrado
    def area(self, lado):
        self.lado = lado
        area = self.lado * self.lado
        return area
        #definir el perimetro de un cuadrado
    def perimetro(self, lado):
        self.lado = lado
        perimetro= 4 * self.lado
        return perimetro




#crear una instancia de la clase cuadrado
cuadrado1 = cuadrado("calcular_area", "calcular_perimetro")
#calcular el area y perimetro de un cuadrado
area_cuadrado1 = cuadrado1.area(6)
perimetro_cuadrado1 = cuadrado1.perimetro(6)
print(f"El area del cuadrado es: {area_cuadrado1}")
print(f"El perimetro del cuadrado es: {perimetro_cuadrado1}")



#crear una instancia de la clase rectangulo
rectangulo1 = rectangulo("calcular_area", "calcular_perimetro") 
#calcular el area y perimetro de un rectangulo
area_rectangulo1 = rectangulo1.area(8, 15)
perimetro_rectangulo1 = rectangulo1.perimetro(8, 15)
print(f"El area del rectangulo es: {area_rectangulo1}")
print(f"El perimetro del rectangulo es: {perimetro_rectangulo1}")
