string = "mi mamá me mima"
contador = 0
print(string.center(40, "="))

contador = string.count("M")
print(f"\nLa letra M se encontro {contador} veces en la cadena: {string}")


contador = string.count("m")
print(f"\nLa letra m se encontro {contador} veces en la cadena: {string}")

contador = string.count("mamá")
print(f"\nLa letra mamá se encontro {contador} veces en la cadena: {string}")

contador = string.count("me mima")
print(f"\nLa oración me mima se encontro {contador} veces en la cadena: {string}")


contador = string.count("ma")
print(f"\nLa palabra ma se encontro {contador} veces en la cadena: {string}")

contador = string.count("m", 13)
print(f"\nLa letra m se encontro {contador} veces, desde la posición 13 en la cadena: {string}")

contador = string.count("m", 100)
print(f"\nLa letra m se encontro {contador} veces, desde la posición 100 en la cadena: {string}")

contador = string.count("m", -3)
print(f"\nLa letra m se encontro {contador} veces, desde la posición -3 en la cadena: {string}")

contador = string.count("m", 3, 7)
print(f"\nLa letra m se encontro {contador} veces, desde la posición 3 hasta la 7 en la cadena: {string}")

contador = string.count("m", 100, 100)
print(f"\nLa letra m se encontro {contador} veces, desde la posición 100 hasta la 100 en la cadena: {string}")

contador = string.count("m", -4, -1)
print(f"\nLa letra m se encontro {contador} veces, desde la posición -4 hasta la -1 en la cadena: {string}")


print(f"\nLa '' se encontro {string.count("")} veces en la cadena: {string}")

