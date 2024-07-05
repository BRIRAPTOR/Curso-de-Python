# Sin utilizar expresiones de comprensión
cuadrados = []
for x in range(10):
    if x % 2 == 0:
        cuadrado = x**2
        cuadrados.append(cuadrado)
print("Sin utilizar expresiones de comprensión: ", cuadrados)

# Con expresiones de comprensión
# [expresión for elemento in iterable if condición]
cuadrados = [x**2 for x in range(10) if x % 2 == 0]
print("Con expresiones de comprensión: ", cuadrados)

# Diccionario creado con expresiones dde comprensión
print("\n\nDiccionario creado con expresiones dde comprensión:")
personas = [("Carlos", 30), ("Gerardo", 25), ("María", 35)]
diccionario_personas = {nombre: edad for nombre, edad in personas if edad >= 30}
print("Diccionario personas:", diccionario_personas)

