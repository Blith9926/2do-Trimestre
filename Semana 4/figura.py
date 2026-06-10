#calcular el area de un cuadrado y rectangulo utilizando clases en python

class figura:
    def __init__(self, calcular_area, calcular_perimetro):
        self.calcular_area = calcular_area
        self.calcular_perimetro = calcular_perimetro
        
#definir el area de un cuadrado
    def area_cuadrado(self, lado):
        self.lado = lado
        area_cuadrado = self.lado * self.lado
        return area_cuadrado
        
#definir el area de un rectangulo
    def area_rectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        area_rectangulo = self.base * self.altura
        return area_rectangulo

class rectangulo(figura):
    def __init__(self, calcular_area, calcular_perimetro):
        super().__init__(calcular_area, calcular_perimetro)





class cuadrado(figura):
    def __init__(self, calcular_area, calcular_perimetro):
        super().__init__(calcular_area, calcular_perimetro)

#crear una instancia de la clase cuadrado
cuadrado1 = cuadrado("calcular_area", "calcular_perimetro")
#calcular el area de un cuadrado
area_cuadrado1 = cuadrado1.area_cuadrado(6)
print(f"El area del cuadrado es: {area_cuadrado1}")

#crear una instancia de la clase rectangulo
rectangulo1 = rectangulo("calcular_area", "calcular_perimetro") 
#calcular el area de un rectangulo
area_rectangulo1 = rectangulo1.area_rectangulo(5, 7)
print(f"El area del rectangulo es: {area_rectangulo1}")
