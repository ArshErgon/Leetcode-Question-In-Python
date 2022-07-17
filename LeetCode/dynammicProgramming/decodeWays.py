



from functools import lru_cache


def decodeWays(string):
    if not string or len(string) == 0:
        return 1

    @lru_cache(None)
    def dfs(string):
        if len(string) > 0:
            if string[0] == '0':
                return 0
        
        if string == "" or len(string) == 1:
            return 1
        
        num = int(string[0:2])
        if num <= 26:
            first = dfs(string[1:])
            second = dfs(string[2:])
            return first + second
        else:
            return dfs(string[1:])

    
    return dfs(string)



print(decodeWays("27"))