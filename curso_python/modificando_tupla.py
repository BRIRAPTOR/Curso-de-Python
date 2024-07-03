tupla = (5, 8, 3, 3, 1, 6, 2)
print(f'Tupla original: {tupla}')
lista = list(tupla)
cont = 0
mod = int(input("¿Cuál de los números quieres modificar por 0?: "))
for i in lista:
    if i == mod:
        lista[cont] = 0
    cont += 1
tupla = tuple(lista)
print(f'Tupla modificada: {tupla}')


