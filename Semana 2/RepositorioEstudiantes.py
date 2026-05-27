import Estudiantes

Estudiantes = []

#Mantenimiento de un CRUD (Create, Read, Update, Delete)

#CREATE
def crearEstudiante():
    try:
        Id = input("Ingrese su Id: ")
        nombre = input("Ingrese su nombre: ")
        Nota = input("Ingrese su Nota: ")
        
        #If 0 <= Nota <= 100:
        #    return Nota
        #else:
        #    print("")
            
        for Estudiante in Estudiantes:
            if Estudiante.Id == Id:
                print("Este Id ya esta en el registro")
                return 
        

        nuevo_Estudiante = Estudiante.Estudiante(Id, nombre,Nota)
        Estudiantes.append(nuevo_Estudiante)  

        print("Estudiante agregado satisfactoriamente")
    
    except ValueError:
        print("Error ; Debe de digitar el Id en numeros")
        

#READ 
def leerEstudiante():
    
    if len(Estudiantes) == 0:
        print("No hay Estudiantes en el sistema")
        return
    
    for Estudiante in Estudiantes:
        Estudiante.mostrarDatos()
    
def buscarEstudiante(Id):
    for Estudiante in Estudiantes:
        if Estudiante.cedula == Id:
            return Estudiante
    
    return None

#UPDATE
def actualizarEstudiante():
    try:
            
        Id = input("Digite su Id: ")
        Estudiante = buscarEstudiante(Id)

        if Id:
            nombre = input("Digite su nuevo nombre: ")

            Estudiante.nombre = nombre
            print("Se ha actualizado con exito")

        else:
            print("No se ha encontrado el Estudiante que quiere modificar.")
    except ValueError:
        print("Error; Estudiante no encontrado")



def eliminarEstudiante():
    try:
            
        Id = input("Digite su Id: ")
        Estudiante = buscarEstudiante(Id)

        if Estudiante:
            Estudiantes.remove(Estudiante)
            print("Se ha eliminado con exito")

        else:
            print("No se ha encontrado el Estudiante que quiere eliminar.")
    except ValueError:
        print("Error; Estudiante no encontrado")
    