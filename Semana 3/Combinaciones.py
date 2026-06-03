import itertools
# EJERCICIO 3 – Generador de combinaciones
# Diferencia entre combinations y permutations:
#   - combinations("AB", 2) → ("A","B")          solo 1 resultado
#   - permutations("AB", 2) → ("A","B"),("B","A") 2 resultados
#   En combinaciones el orden NO importa; en permutaciones SÍ importa.
#   Ejemplo real: "Pan + Café" es la misma promo que "Café + Pan" → combinations.

# Por qué itertools es más eficiente que ciclos manuales:
#   - Está implementado en C dentro del intérprete de Python → más rápido.
#   - Usa iteradores lazy: no ocupa memoria guardando todas las combinaciones
#     a la vez, las genera sobre la marcha.
#   - El código es más corto, legible y menos propenso a errores que
#     anidar múltiples for + condicionales para evitar repetidos.

# Tipo de objeto que devuelve combinations:
#   - Devuelve un objeto iterador (itertools.combinations), NO una lista.
#   - Es "lazy": no genera todos los valores en memoria de una vez,
#     los produce uno por uno a medida que se los solicita.
#   - Para verlos o contarlos hay que recorrerlo (for) o convertirlo (list()).


productos = ["Pan", "Café", "Leche", "Queso"]

# --- Combinaciones de 2 productos ---
# combinations devuelve un iterador; lo convertimos a lista para poder
# recorrerlo más de una vez y usar len() para contar.
promociones_2 = list(itertools.combinations(productos, 2))

print("=" * 40)
print("  Promociones DE 2 PRODUCTOS")
print("=" * 40)
for combo in promociones_2:
    print(f"  {combo[0]}  +  {combo[1]}")

print(f"\nTotal de combinaciones de 2: {len(promociones_2)}")

# --- Combinaciones de 3 productos ---
promociones_3 = list(itertools.combinations(productos, 3))

print("\n" + "=" * 40)
print("  Promociones DE 3 PRODUCTOS")
print("=" * 40)
for combo in promociones_3:
    print(f"  {combo[0]}  +  {combo[1]}  +  {combo[2]}")

print(f"\nTotal de combinaciones de 3: {len(promociones_3)}")

# --- Resumen final ---
print("\n" + "=" * 40)
print("  RESUMEN")
print("=" * 40)
print(f"  Productos disponibles : {len(productos)}")
print(f"  Promociones que se pueden crear con 2 productos : {len(promociones_2)}")
print(f"  Promociones que se pueden crear con 3 productos : {len(promociones_3)}")