


def reorderroutestomakeallpathsleadtothecityzero(n, connections):
    edges = {(a,b) for a,b in connections}
    neighbour = {city:[] for city in range(n)}
    visited = set()
    numberOfChanges = 0

    for a, b in connections:
        neighbour[a].append(b)
        neighbour[b].append(a)


    
    def dfs(city):
        nonlocal numberOfChanges
        for neigh in neighbour[city]:
            if neigh in visited:
                continue
                
            if (neigh, city) not in edges:
                numberOfChanges += 1
            
            visited.add(neigh)

            dfs(neigh)

    visited.add(0)
    dfs(0)

    return numberOfChanges


n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(reorderroutestomakeallpathsleadtothecityzero(n, connections))