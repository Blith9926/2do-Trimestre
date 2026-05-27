from RepositorioEstudiantes import actualizarEstudiante, crearEstudiante, eliminarEstudiante, leerEstudiante

def menu(): 

    while True: 
        print("Mantenimiento de Estudiantes:",
            "1. Crear Estudiante", 
            "2. Leer todos los estudiantes", 
            "3. Actualizar un estudiante", 
            "4. Eliminar un estudiante",
            "5. Salir", sep="\n")
        
        opcion = input("Digite una opcion: ")

        if opcion == "1":
            crearEstudiante()
        elif opcion == "2": 
            leerEstudiante()
        elif opcion == "3":
            actualizarEstudiante()
        elif opcion == "4": 
            eliminarEstudiante()
        elif opcion == "5": 
            break

menu()

