dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }
print(f"Diccionario original: {dictionary}")

last_value = dictionary.pop("b")
print(f"El valor del la clave 'b' eliminado es: {last_value}")

print(f"Diccionario modificado: {dictionary}")

print()

dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }
print(f"Diccionario original: {dictionary}")

last_value = dictionary.pop("z", "No se encuentra la clave dentro del diccionario.")
print(f"El valor del la clave 'z' eliminado es: {last_value}")

print(f"Diccionario modificado: {dictionary}")
