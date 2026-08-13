class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False] * n
        components = 0

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour)
        
        for node in range(n):
            if not visited[node]:
                components += 1
                dfs(node)

        return components
            

        