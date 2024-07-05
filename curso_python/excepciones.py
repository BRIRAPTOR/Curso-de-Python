try:
    numero = int(input('Ingresa un numero: '))
    resultado = 50//numero
    print(f"50/{numero} = {resultado}")
except ValueError as ve:
    print('No es un numero entero: Error!', ve)
except ZeroDivisionError as ze:
    print("No se puede dividir entre cero", ze)
except Exception as e:
    print("Operación no valida", e)
else:
    print("else: - ¡Operación exitosa!")
finally:
    print("Finalizando...")
