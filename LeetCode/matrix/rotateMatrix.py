



def rotateMatrix(matrix, target):

    if target == matrix:
            return True
        # there are 4 different rotation with 90 deg. 
        # We need to check at most 3 more rotation.
    for _ in range(3):
        # transpose the matrixrix by swap row and col values.
        for j in range(len(matrix)):
            for k in range(j+1, len(matrix)):
                matrix[j][k], matrix[k][j] = matrix[k][j], matrix[j][k]
            # Reflect the row by reverse it.
            matrix[j] = matrix[j][::-1]
        # now the matrixrix is roteted; check if they're alike.
        if target == matrix:
            return True
    return False


mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]

print(rotateMatrix(mat, target))