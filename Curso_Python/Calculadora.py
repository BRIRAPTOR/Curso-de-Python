print("Calculadora con una sola variable\n")
print("******************")
print("*Menú de opciones*")
print("******************")
numero = 0

print(" 1. Suma\n 2. Resta\n 3. Multiplicación\n 4. Divición\n 5. Divición entera\n 6. Exponente\n 7. Modulo o resto\n")

numero = int(input("Introduce la opción deseada: "))
if numero == 1:
    print("Elegiste suma")
    numero = int(input("Introduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ",  numero)

elif numero == 2:
    print("Elegiste resta")
    numero = int(input("Introduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", numero)

elif numero == 3:
    print("Elegiste multiplicación")
    numero = int(input("Introduce el primer numero: "))
    numero *= int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", numero)

elif numero == 4:
    print("Elegiste divición")
    numero = float(input("Introduce el primer numero: "))
    numero /= float(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", numero)

elif numero == 5:
    print("Elegiste divición entera")
    numero = int(input("Introduce el primer numero: "))
    numero //= int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", numero)

elif numero == 6:
    print("Elegiste exponente")
    numero = int(input("Introduce el primer numero: "))
    numero **= int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", numero)

elif numero == 7:
    print("Elegiste modulo o resto")
    numero = int(input("Introduce el primer numero: "))
    numero %= int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", numero)

else:
 print("Opción no valida")
