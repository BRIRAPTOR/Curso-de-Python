dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }
print(dictionary)
print(f"\nLos items del diccionario son:\n{dictionary.items()}")

print(f"\nConvirtiendo los items a lista usando el constructor list()")
list_items = list(dictionary.items())

print(f"\nLa lista es {list_items}")
print(f"\nPosición 1 de la lista es {list_items[1]}")
