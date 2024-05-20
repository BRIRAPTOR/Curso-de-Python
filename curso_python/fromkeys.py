# Secuencia con lista sin valor asignado
sequence = ["uno", "dos", "tres"]
dic_name = dict.fromkeys(sequence)
print(f"Secuencia con lista sin valor {dic_name}")


# Secuencia con lista con valor asignado
sequence = ["uno", "dos", "tres"]
value = 5
dic_name = dict.fromkeys(sequence, value)
print(f"Secuencia con lista y valor {dic_name}")


# Secuencia con diccionario
sequence = {"uno": 1, "dos": 2, "tres": 3}
value = 5
dic_name = dict.fromkeys(sequence, value)
print(f"Secuencia con diccionario y valor {dic_name}")

# Secuencia con texto
dic_name = {}.fromkeys("hola", 1)
print(f"Secuencia con texto y valor {dic_name}")

# Secuencia con texto y lista
dic_name = {}.fromkeys("hola", [1, 2, "Hola"])
print(f"Secuencia con texto y valor {dic_name}")

# Secuencia con texto y diccionario
dic_name = {}.fromkeys("hola", {"Juan": 25, "Maria": 22})
print(f"Secuencia con texto y valor {dic_name}")
