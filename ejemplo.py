import os
os.system("cls")


cantidad=int(input("Digite la cantidad de estudiantes: "))

nombre=[]
nota1=[]
nota2=[]
nota3=[]
promedio=[]
estado=[]

#añade un except value error para evitar que el programa se caiga si el usuario ingresa un valor no numerico


for i in range(0, cantidad, 1):
    try:
        nombre.append(input("Nombre del estudiante #"+str(i+1)))
        nota1.append(float(input("Digite la nota 1: ")))
        nota2.append(float(input("Digite la nota 2: ")))
        nota3.append(float(input("Digite la nota 3: ")))
        promedio.append((nota1[i]+nota2[i]+nota3[i])/3)
    except ValueError:
        print("Error: Las notas deben ser números válidos.")




for i in promedio:
    if(i<70):
        estado.append("Reprobado")
    else:
        estado.append("Aprobado")





for g in range (0,cantidad,1):
    print(f"El estudiante {nombre[g]} {estado[g]} con un promedio de {promedio[g]}")