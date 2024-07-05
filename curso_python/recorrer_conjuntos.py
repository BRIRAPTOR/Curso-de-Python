nums = {1, 2, 3, 4, 5}

print("Recorriendo conjunto con el ciclo for:")
for num in nums:
    print(num)

print("Recorriendo conjunto con el ciclo while:")
conjunto_lista = list(nums)
indice = 0
while indice < len(conjunto_lista):
    print(conjunto_lista[indice])
    indice += 1
