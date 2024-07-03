# Ejemplo 1
print("----------Ejemplo 1----------\n")
x = 10
y = 5
print(f"Las coordenadas son: {x}, {y}")
coordenada = tuple([x, y])
print(f"La tupla es: {coordenada}")

print("----------Ejemplo 2----------\n")
string = input("Introduzca un string: ")
string_tuple = tuple(string)
print(f"La tupla es: {string_tuple}")

print("----------Ejemplo 3----------\n")
numbers_dict = {"uno": 1,
                "dos": 2,
                "tres": 3}
print(numbers_dict, "\n")
numbers_tuple = tuple(numbers_dict)
print(f"La tupla es: {numbers_tuple}")

print("----------Ejemplo 4----------\n")
numbers_dict = {"uno": 1,
                "dos": 2,
                "tres": 3}
print(numbers_dict, "\n")
numbers_tuple = tuple(numbers_dict.values())
print(f"La tupla es: {numbers_tuple}")

print("----------Ejemplo 5----------\n")
numbers_dict = {"uno": 1,
                "dos": 2,
                "tres": 3}
print(numbers_dict, "\n")
numbers_tuple = tuple(numbers_dict.items())
print(f"La tupla es: {numbers_tuple}")
