class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        for u,v in prerequisites:
            indegree[u] += 1
            graph[v].append(u)
        

        for course in range(numCourses):
            if indegree[course]:
                continue
            else:
                queue.append(course)
        
        while queue:
            completed = queue.popleft()

            for course in graph[completed]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        for course in range(numCourses):
            if indegree[course] != 0:
                return False
        
        return True





        
        