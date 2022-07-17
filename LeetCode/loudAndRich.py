





def loudAndRich(richer, quietness):
    n = len(quietness)
    graph = [set() for i in range(n)]
    for relation in richer:
        graph[relation[1]].add(relation[0])
    output = [None for i in range(n)]
    for person in range(n):
        if output[person] is None:
            dfs(graph, person, quietness, output)
    return output


def dfs(graph, source, quietness, output):
    leastQuiet = source
    for neighbor in graph[source]:
        if output[neighbor] is None:
            dfs(graph, neighbor, quietness, output)
        
        leastQuiet = min(leastQuiet, output[neighbor], key=lambda x: quietness[x])

    output[source] = leastQuiet


richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]

print(loudAndRich(richer, quiet))