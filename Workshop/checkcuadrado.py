def checksquare(sudoku):

    for linea in sudoku:
        if len(linea) != len(sudoku):
            return False
    return True


correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]

incorrecto5 = [[1, 1.5],
               [1.5, 1]]

print(checksquare(correcto))
print(checksquare(incorrecto6))
print(checksquare(incorrecto5))

