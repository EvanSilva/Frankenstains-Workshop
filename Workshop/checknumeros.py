def checknumeros(sudoku):
    for linea in sudoku:
        for i in linea:
            if not isinstance(i, int):
                return False
    return True
