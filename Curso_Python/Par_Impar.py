print("******************************************************")
print("* Programa que determina si un número es par o impar *")
print("******************************************************\n")

numero = int(input("Por favor introduce un número entero: "))
if numero % 2 == 0:
    print("El número ", numero, "es par.")
else:
    print("El número ", numero, "es impar.")
