print("********** Usando el operador + **********\n")
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(f"Tupla1: {tupla1} | Tupla2: {tupla2}")
tupla_concatenada = tupla1 + tupla2
print(f"Tupla concatenada: {tupla_concatenada}\n")


print("********** Usando el operador += **********\n")
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(f"Tupla1: {tupla1} | Tupla2: {tupla2}")
tupla1 += tupla2
print(f"Tupla1: {tupla1}\n")


print("********** Usando la función tuple() **********\n")
tupla1 = (1, 2, 3)
Lista = [4, 5, 6]
print(f"Tupla1: {tupla1} | Lista: {Lista}")
tupla_concatenada = tupla1 + tuple(Lista)
print(f"Tupla concatenada: {tupla_concatenada}\n")

