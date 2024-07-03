names_tuple = ("Ana", "Gerardo", "María", "Carlos", "Valentina")
print(names_tuple)
lista = list(names_tuple)
bandera = True
while bandera:
    num = int(input("Ingrese un numero entre 0 y 4: "))
    if 0 <= num <= 4:
        print(lista[num])
        bandera = False
    else:
        print("Numero invalido, vuelve a intentar")
