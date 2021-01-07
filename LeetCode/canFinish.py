class Solution:
    def dfs(self, n: int, visited: List) -> bool:
        self.visited.append(n)
        if n in visited:
            return False
        visited.append(n)
        for x in self.adj[n]:
            if not self.dfs(x, visited.copy()):
                return False

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj = []
        self.visited = []
        if not prerequisites:
            return True
        self.stack = [prerequisites[0][0]]
        stack0 = []

        for i in range(numCourses):
            self.adj.append(list(map(lambda x: x[1], filter(lambda x: x[0] == i, prerequisites))))

        for x in range(numCourses):
            if x not in self.visited:
                if not self.dfs(x, []):
                    return False

        return True
