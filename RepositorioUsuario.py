import Usuario

usuarios = []

#Mantenimiento de un CRUD (Create, Read, Update, Delete)

#CREATE
def crearUsuario():

    cedula = input("Ingrese su cedula: ")
    nombre = input("Ingrese su nombre: ")

    for usuario in usuarios:
        if usuario.cedula == cedula:
            print("Esta cedula ya esta en el registro")
            return 

    nuevo_usuario = Usuario.Usuario(cedula, nombre)
    usuarios.append(nuevo_usuario)  

    print("Usuario agregado satisfactoriamente")

#READ 
def leerUsuarios():
    
    if len(usuarios) == 0:
        print("No hay usuarios en el sistema")
        return
    
    for usuario in usuarios:
        usuario.mostrarDatos()
    
def buscarUsuario(cedula):
    for usuario in usuarios:
        if usuario.cedula == cedula:
            return usuario
    
    return None

#UPDATE
def actualizarUsuario():

    cedula = input("Digite su cedula: ")
    usuario = buscarUsuario(cedula)

    if usuario:
        nombre = input("Digite su nuevo nombre: ")

        usuario.nombre = nombre
        print("Se ha actualizado con exito")

    else:
        print("No se ha encontrado el usuario que quiere modificar.")

def eliminarUsuario():
    cedula = input("Digite su cedula: ")
    usuario = buscarUsuario(cedula)

    if usuario:
        usuarios.remove(usuario)
        print("Se ha eliminado con exito")

    else:
        print("No se ha encontrado el usuario que quiere eliminar.")