def adj(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def dfs(n, visited, target, result, words):
    if n == target:
        result.append(len(visited))
    visited.append(n)
    for x in adj(n, words):
        if x not in visited:
            dfs(x, visited.copy(), target, result, words)


def solution(begin, target, words):
    answer = 0
    n = len(begin)
    words = list(filter(lambda x: len(x) == n, words))
    if target not in words:
        return 0
    result = []
    dfs(begin, [], target, result, words)

    return min(result)