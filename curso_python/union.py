conjuntoA = {1, 2, 3}
conjuntoB = {3, 4, 5}
conjuntoC = conjuntoA.union(conjuntoB)
print(conjuntoA)
print(conjuntoB, "\n")
print("Union de conjuntos usando el método .union(): ", conjuntoC)
conjuntoC = conjuntoB | conjuntoA
print("Union de conjuntos usando el operador | : ", conjuntoC)
