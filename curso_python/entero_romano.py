try:
    numero = int(input("Ingresa un numero entero para convertir a romano: "))
    romano = ""
    if 0 < numero < 4000:
        numero = str(numero)
        serie = "123456789"
        longitud = len(numero)
        for ind, i in enumerate(numero):
            if i in serie:
                pos = longitud - ind
                if pos == 4:
                    i = int(i)
                    romano = "M" * i
                elif pos == 3:
                    i = int(i)
                    if i < 4:
                        romano += "C" * i
                    elif i == 4:
                        romano += "CD"
                    elif i == 5:
                        romano += "D"
                    elif 5 < i < 9:
                        i = i - 5
                        romano += "D" + "C" * i
                    elif i == 9:
                        romano += "CM"
                elif pos == 2:
                    i = int(i)
                    if i < 4:
                        romano += "X" * i
                    elif i == 4:
                        romano += "XL"
                    elif i == 5:
                        romano += "L"
                    elif 5 < i < 9:
                        i = i - 5
                        romano += "L" + "X" * i
                    elif i == 9:
                        romano += "XC"
                elif pos == 1:
                    i = int(i)
                    if i < 4:
                        romano += "I" * i
                    elif i == 4:
                        romano += "IV"
                    elif i == 5:
                        romano += "V"
                    elif 5 < i < 9:
                        i = i - 5
                        romano += "V" + "I" * i
                    elif i == 9:
                        romano += "IX"
    else:
        print("El número ingresado debe de estar en un rango entre 1 y 3999")
    print(romano)
except Exception as error:
    print("Debes ingresar un numero entero. ", error)
