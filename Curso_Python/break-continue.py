#Ejemplo para break
print("while con la centencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        break
    print("Valor actual de la variable: ", contador)
print("Fin del programa, la centencia break se ha ejecutado.")



#Ejemplo para continue
print("\while con la centencia continue \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue
    print("Valor actual de la variable: ", contador)
print("Fin del programa, la centencia continue se ha ejecutado.")
