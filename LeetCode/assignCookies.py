




# O(nlogn) || O(1)
def assignCookies(g, s):
    g.sort()
    s.sort()

    i, j = 0, 0
    while i < len(s) and j < len(g):
        if s[i] >= g[j]:
            j += 1
        i += 1
    
    return j


g = [1,2,3]
s = [1,1]

print(assignCookies(g, s))

