import random
print("Piensa en un número entre 1 y 100. Yo tratare de adivinarlo")
anterior = 1
despues = 100
indice = 0
respuesta = ""
try:
    while respuesta != "correcto" and indice < 10:
        if anterior > despues:
            print("Parece que ha habido un error en las respuestas. Por favor, revisa tus indicaciones.")
            break
        indice += 1
        numero_secreto = random.randint(anterior, despues)
        print(f"¿Es {numero_secreto} tu numero?")
        respuesta = input("Ingresa 'mayor', 'menor' o 'correcto': ").lower()
        if respuesta == "mayor":
            anterior = numero_secreto + 1
        elif respuesta == "menor":
            despues = numero_secreto - 1
        elif respuesta == "correcto":
            print(f"¡Adivine tu número secreto {numero_secreto} en {indice} intentos")
            break
        else:
            print("Respuesta no válida. Ingresa 'mayor', 'menor' o 'correcto'.")
    if indice == 10 and respuesta != "correcto":
        print("Lo siento, no pude adivinar tu número en 10 intentos. ¡Mejor suerte la próxima vez!")

except Exception as e:
    print("Operación no valida", e)
finally:
    print("Gracias por jugar")
