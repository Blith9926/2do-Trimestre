#Imagina que deseas crear una clase llamada `Coche` que represente las características
#y el comportamiento de un coche. Vamos a crear la clase `Coche` con atributos como
#marca, modelo, año y velocidad, y métodos para acelerar y frenar el coche

#Paso 1: Definición de la clase

"""Primero, definimos la clase `Coche` con un constructor `__init__` que inicializa los atributos
`marca`, `modelo`, `año` y `velocidad`:"""

class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = 0
        
#Paso 2: Métodos de la clase

    """A continuación, creamos dos métodos dentro de la clase `Coche`. Uno para acelerar el coche
    y otro para frenar:"""

    def acelerar(self, cantidad):
        self.velocidad += cantidad

    def frenar(self, cantidad):
        self.velocidad -= cantidad

          
"""El método `acelerar` recibe un parámetro `cantidad` que representa la cantidad en la que se acelera el coche, y lo suma a la velocidad actual del coche.
El método `frenar` funciona de manera similar, pero reduce la velocidad en lugar de aumentarla."""

#Paso 3: Crear una instancia de la clase

"""Ahora, podemos crear una instancia de la clase `Coche`:"""

mi_coche = Coche("Toyota", "Camry", 2020)


"""Hemos creado un coche con marca "Toyota", modelo "Camry" y año 2020.
La velocidad se inicializa en 0 por defecto."""

#Paso 4: Utilizar los métodos

"""Podemos usar los métodos `acelerar` y `frenar` para modificar la velocidad del coche:"""

mi_coche.acelerar(30)
mi_coche.frenar(10)

"""Hemos acelerado el coche en 30 unidades y luego lo hemos frenado en 10 unidades.
La velocidad actual del coche es ahora 20."""

#Paso 5: Mostrar los resultados

"""Finalmente, podemos mostrar la información del coche, incluyendo su marca, modelo, año y velocidad:"""

print(f"Mi coche es un {mi_coche.marca} {mi_coche.modelo} del año {mi_coche.año}.")
print(f"La velocidad actual es {mi_coche.velocidad} km/h.")


"""Esto imprimirá en la pantalla la información del coche, incluyendo la velocidad actual.

Este es un ejemplo simple de cómo crear una clase en Python, definir atributos y métodos,
y utilizar una instancia de la clase para realizar operaciones."""





