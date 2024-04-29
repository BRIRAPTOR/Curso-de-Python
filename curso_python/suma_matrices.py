matrix_A = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_B = [[1, 5, 3],
            [4, 1, 6],
            [2, 8, 5]]

matrix_C = []

for i in range(len(matrix_A)):
    matrix_C.append([])
    for j in range(len(matrix_A[0])):
        matrix_C[i].append(matrix_A[i][j] + matrix_B[i][j])

for row in range(len(matrix_A)):
    if row == 1:
        print(f"{matrix_A[row]} + {matrix_B[row]} = {matrix_C[row]}")
    else:
        print(f"{matrix_A[row]}   {matrix_B[row]}   {matrix_C[row]}")
