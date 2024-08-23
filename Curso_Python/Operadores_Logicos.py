#Conjunción
print("Conjunción (and)")

num_uno = int(input("Escribe un numero mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("El numero ", num_uno, " cumple con la condición.\n")
else:
    print("El numero ", num_uno, " NO cumple con la condición.\n")

#Disyunción

print("Disyunción (or)")

palabra = input("Para complir con la condición escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido.\n")
else:
    print("La condición no se ha cumplido.\n")

#Negación
print("Negación (not)")
num_uno = int(input("Introduce un numero igual a 5: "))
if not num_uno == 5:
    print("\n El numero es diferente de 5 y Si se cumple la condición.\n")
else:
    print("\n El numero es igual de 5 y No se cumple la condición.\n")
