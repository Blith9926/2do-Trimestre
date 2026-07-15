import sqlite3
NombreDb = 'usuarios.db'

def obtener_conexion():
    conexion = sqlite3.connect(NombreDb)
    return conexion

def crearTablaUsuario():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            cedula TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            anno_nacimiento INTEGER NOT NULL,
            mes_nacimiento INTEGER NOT NULL,
            dia_nacimiento INTEGER NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()