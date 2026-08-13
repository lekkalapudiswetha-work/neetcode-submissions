class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        result = []

        for u,v in prerequisites:
            graph[u].append(v)
        
        def dfs(node,target,visited):
            if node in visited:
                return False
            visited.add(node)
            for course in graph[node]:
                if course == target:
                    return True
                if dfs(course,target,visited):
                    return True
            return False
        
        for prerequisite,course in queries:
            visited = set()
            result.append(dfs(prerequisite,course,visited))
        
        return result
