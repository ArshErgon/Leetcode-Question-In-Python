class Solution:
    def generateMatrix(self, n):
        if not n:
            return []
        
    
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        # create an empty n*n matrix
        
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        count = 1
        
        while left <= right and top <= bottom:
            
            for i in range(left, right):
                matrix[top][i] = count
                count += 1
            
            top += 1
            
            for i in range(top, bottom):
                matrix[i][right - 1] = count
                count += 1
                
            right -= 1
            
            for i in reversed(range(left, right)):
                matrix[bottom - 1][i] = count
                count += 1
                
            bottom -= 1
            
            for i in reversed(range(top, bottom)):
                matrix[i][left] = count 
                count += 1
            left += 1
            
        return matrix