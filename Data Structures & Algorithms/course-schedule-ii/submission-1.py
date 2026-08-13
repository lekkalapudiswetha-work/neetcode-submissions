class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        result = []
        finished = 0

        for u,v in prerequisites:
            indegree[u] += 1
            graph[v].append(u)
        

        for course in range(numCourses):
            if indegree[course]:
                continue
            else:
                # result.append(course)
                queue.append(course)
        
        while queue:
            completed = queue.popleft()
            result.append(completed)
            finished += 1

            for course in graph[completed]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return result if finished == numCourses else []