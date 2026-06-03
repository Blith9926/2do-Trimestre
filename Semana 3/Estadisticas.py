import statistics 

notas = [85, 90, 78, 92, 88, 76, 95]

#calcular el promedio, la mediana, la media y la desviacion estandar de las notas
promedio = statistics.mean(notas)
mediana = statistics.median(notas)
moda = statistics.mode(notas)
desviacion_estandar = statistics.stdev(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Desviación Estándar: {desviacion_estandar:.2f}")

#Determinar si el grupo tiene alta variabilidad (si la desviación es mayor a 8). 
if desviacion_estandar > 8:
    print("El grupo tiene alta variabilidad.")
else:
    print("El grupo tiene baja variabilidad.")
    
#La desviación estándar es una medida de dispersión que indica cuánto varían los datos respecto a su media. Si la desviación estándar es alta, significa que los datos están más dispersos y hay una mayor variabilidad en el grupo. En este caso, si la desviación estándar es mayor a 8, se considera que el grupo tiene alta variabilidad.
#AL diferencia entre media y mediana es que la media es el promedio de los datos, mientras que la mediana es el valor central cuando los datos están ordenados. 
#cada medida se usaria en diferentes situaciones: la media es útil para datos simétricos sin valores atípicos, mientras que la mediana es más robusta y se prefiere cuando hay valores extremos o datos sesgados. el promedio es útil para obtener una idea general del rendimiento del grupo, mientras que la mediana puede ser más representativa si hay estudiantes con notas muy bajas o muy altas que podrían distorsionar el promedio. La moda puede ser útil para identificar la nota más común entre los estudiantes. y la desviacion estandar es importante para entender la variabilidad de las notas y si el grupo tiene un rendimiento homogéneo o heterogéneo.