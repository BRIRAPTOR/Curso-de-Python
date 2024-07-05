import random
print("Bienvenido a Adivina Numero Secreto")
print("He seleccionado un número entre 1 y 100. ¡Adivina cuál es!")
numero_secreto = random.randint(1, 100)
indice = 0
numero = 0
try:
    while numero_secreto != numero and indice != 10:
        indice += 1
        print(f"Intento {indice}/10")
        try:
            numero = int(input("Ingresa tu adivinanza: "))
        except ValueError as ve:
            print("Ingresa un numero entero entre 1 y 100", ve)
            continue
        if indice == 10 and numero != numero_secreto:
            print(f"Lo siento, el número secreto era {numero_secreto}. ¡Mejor suerte la próxima vez!")
        elif numero == numero_secreto:
            print(f"Felicidades! ¡Has adivinado el número secreto {numero_secreto} en {indice} intentos")
        elif numero < numero_secreto:
            print("El numero secreto es mayor")
        elif numero > numero_secreto:
            print("El numero secreto es menor")

except Exception as e:
    print("Operación no valida", e)
finally:
    print("Gracias por jugar")
