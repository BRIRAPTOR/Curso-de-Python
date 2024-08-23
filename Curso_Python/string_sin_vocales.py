string = input("Introduce una frace: ")
letra = input("¿Con quie letra deseas terminar el bucle?: ")
substring = ""
for indice in string:
    if indice.lower() != letra.lower():
         if indice.lower() != "a" and indice.lower() != "e" and indice.lower() != "i" and indice.lower() != "o" and indice.lower() != "u":
            substring += indice
    else:
         break               
print(substring)
