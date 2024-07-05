conjuntoA = {1, 2, 3, 4, 5}
conjuntoB = {4, 5, 6, 7, 8}
print(conjuntoA)
print(conjuntoB, "\n")
diferencia_simetrica = conjuntoA.symmetric_difference(conjuntoB)
print(f"Diferencia simétrica conjuntoA.symmetric_difference(conjuntoB): {diferencia_simetrica}\n")

diferencia_simetrica_operador = conjuntoA ^ conjuntoB
print(f"Diferencia simétrica conjuntoA ^ conjuntoB: {diferencia_simetrica_operador}")
