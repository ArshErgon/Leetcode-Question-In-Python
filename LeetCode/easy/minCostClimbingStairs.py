


def minCostClimbingStairs(cost):
    if not cost:
        return 0

    current = next = 0
    for i in reversed(range(len(cost))):
        current, next = next, min(next, current) + cost[i]
    return min(current, next)
    
    # dp = [0] * len(cost)

    # dp[0] = cost[0]

    # if len(cost) > 1:
    #     dp[1] = cost[1]

    # for i in range(2, len(cost)):
    #     dp[i] = cost[i] + min(dp[i-2], dp[i-1])

    # return min(dp[-2], dp[-1])


print(minCostClimbingStairs([10, 15, 20]))