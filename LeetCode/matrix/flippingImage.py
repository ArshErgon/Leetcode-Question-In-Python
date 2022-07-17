from re import S


class Solution:
    def flipAndInvertImage(self, image):
        
        def reverse(image):
            for row in range(len(image)):
                image[row] = image[row][::-1]
                
        
        reverse(image)
        
        
        for row in range(len(image)):
            for col in range(len(image[row])):
                if image[row][col] == 1:
                    image[row][col] = 0
                    
                else:
                    image[row][col] = 1
                    
        return image

sol = Solution()
print(sol.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))