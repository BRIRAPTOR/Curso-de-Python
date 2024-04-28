numeros = int(input("¿Cuantos números contendrá la lista?: "))
i = 0
lista = []
while i < numeros:
    lista.append(int(input("Introduce un número entero: ")))
    i = i + 1
print(f"\n{lista}")
print(f"La suma total de los elementos es: {sum(lista)}")
