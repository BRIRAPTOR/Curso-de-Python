print("Introduce dos números a comparar: \n")

num_uno = int(input("Introduce el primer número: "))
num_dos = int(input("Introduce el segundo número: "))

print("Los numeros a comparar son: " , num_uno ," y " , num_dos)
if num_uno == num_dos:
    print("Es igual...")
if num_uno != num_dos:
    print("Es diferente...")
if num_uno >= num_dos:
    print("Es mayor o igual...")
if num_uno <= num_dos:
    print("Es menor o igual...")
if num_uno > num_dos:
    print("Es mayor...")
if num_uno < num_dos:
    print("Es menor...")

