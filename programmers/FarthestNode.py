def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n + 1)]
    visited = [False for i in range(n + 1)]
    visited[1] = True
    queue = [1]
    distance = [0 for i in range(n + 1)]
    for (x, y) in edge:
        graph[x].append(y)
        graph[y].append(x)

    while queue:
        n = queue.pop(0)
        for x in graph[n]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)
                distance[x] = distance[n] + 1

    return distance.count(max(distance))