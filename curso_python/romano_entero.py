try:
    romano = input("Ingresa un numero romano para convertir a entero: ").upper()
    numero = 0
    valores_romanos = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]

    i = 0
    while i < len(romano):
        for valor, simbolo in valores_romanos:
            if romano[i:i+len(simbolo)] == simbolo:
                numero += valor
                i += len(simbolo)
                break
        else:
            print("Símbolo romano inválido:", romano[i])
            break
    print(numero)
except Exception as e:
    print("Ingresa un número romano válido para convertir a entero: ", e)
