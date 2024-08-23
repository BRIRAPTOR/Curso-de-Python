print("=========")
print("Conversor")
print("=========")
print("")
print("Menú de opciones:")
print("")
print("Preciona 1 para convertir de número a palabra. ")
print("Preciona 2 para convertir de palabra a número. ")
num_uno = int(input("¿Cuál es tu opción deseada?: "))
if num_uno == 1:
    
    print("¡¡Convertidor de numeros a letras!!")
    num_uno = int(input("¿Cuál es el numero que deseas convertir?: "))
    if num_uno == 1:
        print("El número es 'Uno'")
        print("Fin.")
    elif num_uno == 2:
        print("El número es 'Dos'")
        print("Fin.")
    elif num_uno == 3:
        print("El número es 'Tres'")
        print("Fin.")
    elif num_uno == 4:
        print("El número es 'Cuatro'")
        print("Fin.")
    elif num_uno == 5:
        print("El número es 'Cinco'")
        print("Fin.")
    else:
        print("Este programa solo puede convertir hasta el número 5")
        print("Fin.")

    
elif num_uno == 2:
    
    print("¡¡Convertidor de letras a numeros!!")

    palabra_uno = input("¿Cuál es la palabra que deseas convertir?: ")
    palabra_uno = palabra_uno.lower()
    
    if palabra_uno == 'uno':
        print("El número es '1'")
        print("Fin.")
    elif palabra_uno == 'dos':
        print("El número es '2'")
        print("Fin.")
    elif palabra_uno == 'tres':
        print("El número es '3'")
        print("Fin.")
    elif palabra_uno == 'cuatro':
        print("El número es '4'")
        print("Fin.")
    elif palabra_uno == 'cinco':
        print("El número es '5'")
        print("Fin.")
    else:
        print("Este programa solo puede convertir hasta el número 5")
        print("Fin.")

else:
    print("Opción no valida")
    print("Fin.")
