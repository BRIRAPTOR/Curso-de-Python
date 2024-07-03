conjuntoA = {1, 2, 3, 4, 5}
conjuntoB = {4, 5, 6, 7, 8}
print(conjuntoA)
print(conjuntoB, "\n")

diferencia_conjuntosAB = conjuntoA.difference(conjuntoB)
print(f"conjunto_A.difference(conjuntoB): {diferencia_conjuntosAB}")
print()
diferencia_conjuntosBA = conjuntoB - conjuntoA
print(f"conjunto_B - conjuntoA: {diferencia_conjuntosBA}")


