



# O(n) || O(1)
def climbingStairs(n):
    if n <= 2:
        return n

    first, second = 1, 2

    for i in range(2, n + 1):
        first, second = second, second + first

    return first


print(climbingStairs(5))


# O(n) || O(n)
def climbingStairsWithDynammicProgramming(n):
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 2

    for i in range(2, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    
    return dp[n-1]


print(climbingStairsWithDynammicProgramming(5))
