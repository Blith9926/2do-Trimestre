from datetime import datetime
from datetime import date

anno = int(input("Ingrese su anno de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))
dia = int(input("Ingrese su dia de nacimiento: "))

fecha_nacimiento = date(anno, mes, dia)
fecha_actual = date.today()
edad = fecha_actual.year - fecha_nacimiento.year

print(f"Su edad es: {edad}")

dias_vida = (fecha_actual - fecha_nacimiento).days
print(f"Usted ha vivido {dias_vida} dias")

proximo_cumple = date(fecha_actual.year, mes, dia)
if proximo_cumple < fecha_actual:
    proximo_cumple = date(fecha_actual.year + 1, mes, dia)
dias_para_cumple = (proximo_cumple - fecha_actual).days
print(f"Faltan {dias_para_cumple} dias para su proximo cumpleaños")


# Al restar dos fechas nos indica la cantidad de días entre ellas.
#Se usa datetime.date para poder calcular el número de días vividos y los días restantes para el próximo cumpleaños. Ya que no se pueden combinar datetime con date
#El proximo cumpleaños se calcula comparando la fecha actual con la fecha del cumpleaños de este año. Si ya pasó, se calcula para el próximo año.
