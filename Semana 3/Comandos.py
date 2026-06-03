import os

import pip
pip install pyreadline3


# EJERCICIO 4 – Historial de comandos interactivo 
# Librería: pyreadline3 (Windows)
# Instalación: pip install pyreadline3

# Qué ventaja aporta pyreadline3:
#   - Permite navegar el historial de comandos con las teclas ↑ y ↓
#     sin escribir código extra; el sistema lo maneja automáticamente.
#   - Habilita edición de línea: moverse con ←→, borrar con Backspace,
#     ir al inicio/fin con Home/End, todo dentro del input().
#   - Soporta autocompletado personalizable con tab (no usado aquí).
#   - Permite guardar y cargar el historial desde un archivo entre sesiones.
#
# En qué sistemas operativos funciona:
#   - pyreadline3 es la versión para Windows del módulo readline.
#   - readline nativo funciona en Linux y macOS (viene con Python).
#   - pyreadline3 replica esa funcionalidad en Windows mediante
#     pip install pyreadline3.
#
# Cómo mejora la experiencia del usuario?
#   - Sin pyreadline3: hay que reescribir cada comando desde cero.
#   - Con pyreadline3: ↑ recupera el comando anterior, ↓ avanza,
#     se puede editar y reejecutar → igual que cualquier terminal
#     profesional (cmd mejorado, PowerShell, bash, etc.).


# Importación de pyreadline3
try:
    from pyreadline3 import Readline
    readline = Readline()
    READLINE_DISPONIBLE = True
except ImportError:
    READLINE_DISPONIBLE = False
    print("ERROR: pyreadline3 no está instalado.")
    print("       Ejecutá: pip install pyreadline3")
    print("       El programa continuará SIN historial de navegación.\n")

# Configuración del historial
if READLINE_DISPONIBLE:
    # Límite máximo de entradas guardadas en el historial
    readline.set_history_length(100)

# Bucle principal de la consola
print("=" * 45)
print("   CONSOLA INTERACTIVA CON HISTORIAL")
print("=" * 45)
if READLINE_DISPONIBLE:
    print("Tip: usá ↑ / ↓ para navegar el historial.")
print("Escribí 'salir' para terminar.")

contador = 1  # Contador de comandos para mostrar en el prompt

while True:
    try:
        # input() con pyreadline3 activo ya soporta flechas e historial
        comando = input(f"cmd[{contador}]> ").strip()
    except (EOFError, KeyboardInterrupt):
        # Ctrl+C → salida limpia
        print("\nSesión finalizada.")
        break

    # Comando vacío: no contar ni procesar
    if not comando:
        continue

    # Condición de salida
    if comando.lower() == "salir":
        print("Saliendo de la consola. ¡Hasta luego!")
        break

    # Procesamiento de comandos de ejemplo
    if comando.lower() == "ayuda":
        print("  Comandos disponibles: ayuda, historial, limpiar, salir")

    elif comando.lower() == "historial":
        if READLINE_DISPONIBLE:
            total = readline.get_current_history_length()
            print(f"  Historial ({total} entradas):")
            for i in range(1, total + 1):
                print(f"    {i}: {readline.get_history_item(i)}")
        else:
            print("  Historial no disponible (pyreadline3 no instalado).")

    elif comando.lower() == "limpiar":
        if READLINE_DISPONIBLE:
            readline.clear_history()
        os.system("cls")
        contador = 0

    else:
        print(f"  Comando recibido: '{comando}'")

    contador += 1