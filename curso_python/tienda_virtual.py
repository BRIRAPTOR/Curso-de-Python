print("Bienvenido a la Tienda Virtual")
opcion = 1
carrito = {}
total = 0
productos = {
    # Cantidad en stock, producto, precio
    1: [50, "Camiseta", 20],
    2: [50, "Jeans", 30],
    3: [50, "Zapatos", 20],
    4: [50, "Sombrero", 20],
    5: [50, "Chamarra", 20]
    }
try:
    while opcion != 0:
        print("Menú")
        print("1. Agregar productos al carrito.")
        print("2. Ver carrito.")
        print("3. Realizar el pago y salir.")
        print("0. Salir.")
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError as ve:
            print("Opción no valida. Por favor, ingrese una opción del menu.", ve)
            continue
        if opcion == 1:
            for key, product in productos.items():
                print(f"El id {key}, {product[0]} x {product[1]} ${product[2]}")
            producto = input("Ingrese el nombre del producto: ").capitalize()
            producto_encontrado = False
            for key, product in productos.items():
                if product[1] == producto:
                    if product[0] > 0:
                        product[0] -= 1
                        if key in carrito:
                            carrito[key][0] += 1
                        else:
                            carrito[key] = [1, product[1], product[2]]
                        print(f"{product[1]} agregado al carrito.")
                    else:
                        print(f"Lo sentimos, {product[1]} está agotado.")
                    producto_encontrado = True
                    break
            if not producto_encontrado:
                print("El producto no existe.")
        elif opcion == 2:
            print("Carrito: ")
            total = 0
            for key, product in carrito.items():
                print(f"El id {key}, {product[0]} x {product[1]} ${product[2]}")
                total += product[0] * product[2]
            print(f"Total: ${total}")
        elif opcion == 3:
            print(f"Total a pagar: ${total}")
            try:
                monto = int(input("Ingrese el monto con el que pagará: "))
                if monto > total:
                    cambio = monto - total
                    print(f"Gracias por su compra. Su cambio es: ${cambio}")
                    print("Saliendo.")
                    opcion = 0
                elif monto < total:
                    print("El monto ingresado es insuficiente. Por favor, ingrese un monto válido.")
                elif monto == total:
                    print("El monto ingresado es correcto. Gracias por su compra.")
                    print("Saliendo.")
                    opcion = 0
                else:
                    print("Monto inválido. Por favor, ingrese un monto válido.")
            except ValueError as ve:
                print("Monto inválido. Por favor, ingrese un monto válido.", ve)
                continue
        elif opcion == 0:
            print("Saliendo.")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            continue

except Exception as e:
    print("Operación no válida. Por favor, seleccione una opción válida.", e)
