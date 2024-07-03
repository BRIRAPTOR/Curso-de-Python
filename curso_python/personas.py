tupla_personas = (("Eduardo", 26), ("María", 30), ("Gerardo", 20), ("Valentina", 22))
print(tupla_personas)
indice = 0
mayor_edad = 0
menor_edad = 0
mayor_indice = 0
menor_indice = 0
for nombre, edad in tupla_personas:
    if edad > mayor_edad:
        mayor_edad = edad
        mayor_indice = indice
    indice += 1
print(f"La persona  mayor edad: {tupla_personas[mayor_indice]}")
indice = 0
for nombre, edad in tupla_personas:
    if indice == 0:
        menor_edad = edad
    if edad < menor_edad:
        menor_edad = edad
        menor_indice = indice
    indice += 1
print(f"La persona  menor edad: {tupla_personas[menor_indice]}")
