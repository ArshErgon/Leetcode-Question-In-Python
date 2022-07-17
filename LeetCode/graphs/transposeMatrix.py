



# def transposeMatrix(matrix):
#     return list(map(list, zip(*matrix)))

def transposeMatrix(matrix):
    if not matrix:
        return None
    # return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    result = []
    for row in range(len(matrix[0])):
        newList = []
        for col in range(len(matrix)):
            newList.append(matrix[col][row])
        result.append(newList)

    return result

print(transposeMatrix([[1,2,3],[4,5,6]]))