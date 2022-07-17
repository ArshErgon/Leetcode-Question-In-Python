


# O(n)
def triangle(array):
    if not array:
        return 0
    
    dp = [0] * (len(array) + 1)

    for i in reversed(range(len(array))):
        for idx, val in enumerate(array[i]):
            dp[idx] = min(dp[idx], dp[idx + 1]) + val

    return dp[0]





print(triangle([[2],[3,4],[6,5,7],[4,1,8,3]]))
# print(triangle([[-10]]))
print(triangle([[-1],[2,3],[1,-1,-3]]))



