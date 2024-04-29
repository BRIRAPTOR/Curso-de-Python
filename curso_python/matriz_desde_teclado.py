rows = int(input("¿Cuantas filas tendrá la matriz?: "))
columns = int(input("¿Cuantas columnas tendrá la matriz?: "))
matrix = []
for i in range(rows):
    matrix.append([])
    for j in range(columns):
        matrix[i].append(int(input(f"Introduce un eleménto a la fila {i} y la columna {j}: ")))

print("Mostrar todos los elementos de una matriz en formato de matriz")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

