mensaje = "Hola"
mensaje += " "
mensaje += "Brian"
print(mensaje)

print("Concatenación")

mensaje = "Hola"
espacio = " "
nombre = "Brian"
print(mensaje + espacio + nombre)

numero_uno = 6
numero_dos = 4
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

print("Busqueda:")

mensaje = "Hola Brian"
buscar_subcadena = mensaje.find("Brian")
print(buscar_subcadena)

print("Extracción")
mensaje = "Hola Brian"
extraer_cadena = mensaje[1:8]
print(extraer_cadena)

print("Comparación")

mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)
