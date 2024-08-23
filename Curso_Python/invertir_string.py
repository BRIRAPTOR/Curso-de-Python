string = input("Introduce un string para invertirlo: ")
longitud = len(string)
substring = ""
for character in string:
    substring += string[longitud - 1 : longitud]
    longitud = longitud - 1
print(f"String invertido: {substring}")
