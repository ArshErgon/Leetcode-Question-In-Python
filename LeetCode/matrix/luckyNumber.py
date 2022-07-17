



def luckyNumber(matrix):
    minRow = [min(r) for r in matrix]
    maxCol = [max([matrix[r][c] for r in range(len(matrix))]) for c in range(len(matrix[0]))]
    return [rv for cv in minRow for rv in maxCol if cv == rv]


matrix = [[3,7,8],[9,11,13],[15,16,17]]

print(luckyNumber(matrix))