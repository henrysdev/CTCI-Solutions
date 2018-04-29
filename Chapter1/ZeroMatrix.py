"""
Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column are set to O.
"""
def zeroMatrix(matrix):
    zeros = []
    for row, y in enumerate(matrix):
        for elem, x in enumerate(row):
            if elem == 0:
                zeros.push_back((y,x))

    for zero in zeros:
        matrix[zero[0]] *= 0
        for row in matrix:
            row[zero[1]] *= 0

    return matrix