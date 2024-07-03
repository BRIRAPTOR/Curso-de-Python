conjunto_A = {1, 2, 3}
conjunto_B = {4, 5, 6, 7, 8}
print(conjunto_A)
print(conjunto_B, "\n")

# Utilizando el método intersection()
intersection_conjuntos = conjunto_A.intersection(conjunto_B)

# Utilizando el operador &
intersection_conjuntos_operador = conjunto_B & conjunto_A
print("Intersection conjuntos Utilizando el método intersection(): ", intersection_conjuntos)
print("Intersection conjuntos Utilizando el operador &: ", intersection_conjuntos_operador)
