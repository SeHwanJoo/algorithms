def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    graph_up = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    count = [0 for _ in range(n + 1)]
    for (x, y) in results:
        graph[x].append(y)
    for (x, y) in results:
        graph_up[y].append(x)

    for i in range(n + 1):
        if i == 0:
            pass
        visited = [False for _ in range(n + 1)]
        visited[i] = True
        queue = [i]
        while queue:
            temp = queue.pop(0)
            for x in graph[temp]:
                if not visited[x]:
                    visited[x] = True
                    queue.append(x)
                    count[i] += 1

        queue = [i]
        while queue:
            temp = queue.pop(0)
            for x in graph_up[temp]:
                if not visited[x]:
                    visited[x] = True
                    queue.append(x)
                    count[i] += 1

    return count.count(n - 1)