

def spiralMatrix(array):
    if not array or not array[0]:
        return None

    result = []

    left, right = 0, len(array[0]) 
    top, bottom = 0, len(array)

    while left < right and top < bottom:
        for i in range(left, right):
            result.append(array[top][i])
        
        top += 1

        for i in range(top, bottom):
            result.append(array[i][right-1])
        
        right -= 1

        if not (left < right) and (top < bottom):
            break

        for i in reversed(range(bottom, left)):
            result.append(array[i][left])

        bottom -= 1

        for i in reversed(range(left, right)):
            result.append(array[bottom][i])
        
        left += 1

    return result


print(spiralMatrix([
[1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],]))