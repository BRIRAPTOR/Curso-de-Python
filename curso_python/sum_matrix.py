num_matrices = int(input("¿Cuantas matrices vamos a sumar?: "))
rows = int(input("¿Cuantas filas tendrá la matriz?: "))
columns = int(input("¿Cuantas columnas tendrá la matriz?: "))
matrices = []
for io in range(num_matrices):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(int(input(f"Introduce un eleménto a la matriz {io} a la fila {i} y la columna {j}: ")))
    matrices.append(matrix)

matrix_C = [[0 for _ in range(columns)] for _ in range(rows)]
for matrix in matrices:
    for i in range(rows):
        for j in range(columns):
            matrix_C[i][j] += matrix[i][j]

for i in range(rows):
    for matrix in matrices:
        print(matrix[i], end=' + ')
    print('=', matrix_C[i])



