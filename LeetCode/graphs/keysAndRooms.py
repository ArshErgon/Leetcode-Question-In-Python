

# O(n) || O(n)
def keysAndRooms(rooms):
    seen = set()
    stack = [0]
    seen.add(0)
    while stack:
        cur = stack.pop()
        for neigh in rooms[cur]:
            if not neigh in seen:
                seen.add(neigh)
                stack.append(neigh)

    return len(seen) == len(rooms)




print(keysAndRooms([[1],[2],[3],[]]))
print(keysAndRooms([[1,3],[3,0,1],[2],[0]]))

