tupla1 = (1, 2, 3, 4, 5)
tupla2 = (8, 6, 4, 2, 0)
print(f"Tupla 1: {tupla1}")
print("+")
print(f"Tupla 2: {tupla2}")
print("=========================")
tupla_resul = []
for i in range(len(tupla1)):
    tupla_resul.append(tupla1[i] + tupla2[i])
print(f"Suma     {tuple(tupla_resul)}")
