class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)
        visited = [False] * (n+1)
        cycle = set()
        cyclestart = -1

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node,par):
            nonlocal cyclestart
            if visited[node]:
                cyclestart = node
                return True
            
            visited[node] = True
            for nei in graph[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    if cyclestart != -1:
                        cycle.add(node)
                    if node == cyclestart:
                        cyclestart = -1
                    return True
            return False
        
        dfs(1,-1)

        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        
        return []



        

        
        