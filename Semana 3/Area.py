import math

# Solicitar el radio al usuario y convertirlo a número decimal (float)
radio = float(input("Introduce el radio del círculo: "))

# Calcular el área
area = math.pi * (radio ** 2)

# Mostrar el resultado
print(f"El área del círculo con radio {radio} es: {area:.2f}")


# Cálculos
#area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

# Mostramos los resultados (limitando a 2 decimales para mayor legibilidad)
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

# otra forma para redondear

area_redondeada = round(area, 2)
perimetro_redondeado = round(perimetro, 2)

print("Área:", area_redondeada)
print("Perímetro:", perimetro_redondeado)


#print(math.pow(9, 0.5))
#para elevar a la potencia de 3
print(2 ** 3)        # 8 (int)

print(math.pow(2, 3))

#sdfasf

#resultado = 2 ** 3  # 8
#Funciona con enteros, flotantes y números complejos.
#Mantiene el tipo de dato cuando es posible (si ambos son int y el resultado cabe en un entero, devuelve int).

#resultado = math.pow(2, 3)  # 8.0
#Siempre devuelve un float, incluso si los argumentos son enteros.
#Solo acepta números reales (int o float), no complejos.
#""""