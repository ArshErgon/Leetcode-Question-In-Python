

# O(n) || O(n)
def partationLables(string):
    if not string:
        return string
    
    indices = {char:idx for idx, char in enumerate(string)}

    start = 0
    end = 0
    newList = []
    for idx, char in enumerate(string):
        end = max(end, indices[char])
        if idx == end:
            newList += [end - start + 1]
            start = end + 1
    
    return newList

s = "ababcbacadefegdehijhklij"
print(partationLables(s))

