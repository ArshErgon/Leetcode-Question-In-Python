
# O(n^2) || O(n)
def pascalTriangle(num):
    if not num:return []
    if num == 1:
        return [[1]]
    
    if num == 2:
        return [[1], [1, 1]]

    dp = [[1], [1, 1]]

    for i in range(2, num):
        dp.append([1])
        for j in range(1, i):
            dp[i].append(dp[i-1][j-1]+dp[i-1][j])
        dp[i].append(1)

    return dp

print(pascalTriangle(5))