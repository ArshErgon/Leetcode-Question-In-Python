class Solution:
    def arrangeCoins(self, n: int) -> int:
        return self.optimalOne(n)
        return self.bruteForce(n)
    
# O(1) || O(1) 
# runtime: 48ms 69.84%
# memory: 13.9mb 56.52%
# 1 + 2 + 3 + 4 ... n = n (n + 1) / 2 is a series 
# where n is equal to the last term of our series and also represents the number of terms.
# so all we need is just solve the equation n = i*(i + 1)/2
    def optimalOne(self, coins):
        return int(((0.25 + 2 * coins) ** 0.5) - 1/2)

    
#     O(n) || O(1)
#    Runtime: 1724ms 8.29%; memory: 13.8mb 96.45%
    def bruteForce(self, coins):
        
        if not coins:
            return coins

        if coins == 1:return coins

        total = 0
        k = 1

        while coins >= 0:
            coins -= k
            k += 1
            total += 1

        return total - 1