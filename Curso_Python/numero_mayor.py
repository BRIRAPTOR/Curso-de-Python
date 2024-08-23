print("*************************************************************************")
print("* Programa para determinar ¿Cuál es el numero más grande de tres números?")
print("*************************************************************************")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if num1 > num2 and num1 > num3 :
        print("El número ", num1, " es el número más grande de los tres" )
elif num2 > num1 and num2 > num3:
        print("El número ", num2, " es el número más grande de los tres" )
else:
        print("El número ", num3, " es el número más grande de los tres" )
