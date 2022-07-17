

def searchMatrix(matrix, target):
    col = len(matrix[0]) - 1
    for index in range(len(matrix)):
        print(matrix[index][col])
        while matrix[index][col] > target and col >= 0:
            print(matrix[index][col])
            col -= 1

        if matrix[index][col] == target:
            return True
        
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 30))