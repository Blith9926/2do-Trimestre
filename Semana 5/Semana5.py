entrada = "     usuario: Diego | edad: 28 | pais: CR   "
print(entrada)
entrada = entrada.strip().capitalize()
print(entrada)
nombre = entrada[8:14]
nombre = nombre.upper()
print(f"El nombre de usuario es: {nombre}")
edad = entrada[23:25]
print(f"La edad del usuario es: {edad}")