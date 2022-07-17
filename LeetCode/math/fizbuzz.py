class Solution:
#     O(n) || O(n)
# Runtime: 44ms 90.88ms ; Memory: 14.9mb 84.93%
    def fizzBuzz(self, n):
        result = []
        
        for i in range(1, n + 1):
            if i % 15 == 0:
                char = "FizzBuzz"
            elif i % 3 == 0:
                char = "Fizz"
            elif i % 5 == 0:
                char = "Buzz"
            else:
                char = str(i)
            result.append(char)
        
        return result