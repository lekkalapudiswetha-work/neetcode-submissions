class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights) , len(heights[0])
        result = []
        queue_pacific = deque()
        queue_atlantic = deque()

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        for i in range(cols):
            pacific[0][i] = True
            queue_pacific.append((0,i))
        
        for i in range(1,rows):
            pacific[i][0] = True
            queue_pacific.append((i,0))
        
        for i in range(cols):
            atlantic[rows-1][i] = True
            queue_atlantic.append((rows-1,i))
        
        for i in range(rows-1):
            atlantic[i][cols-1] = True
            queue_atlantic.append((i,cols-1))
        
        directions = [
            [1,0],[-1,0],[0,1],[0,-1]
        ]
        # print(queue_pacific,queue_atlantic)
        # print(pacific,atlantic)

        def bfs(queue,ocean):
            while queue:
                r ,c = queue.popleft()
                

                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    # if nr == 1 and nc == 4:
                        # print(r,c,nr,nc)
                        # print(0 <= nr < rows and 0 <= nc < cols and heights[r][c] <= heights[nr][nc] and not ocean[nr][nc])

                    if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and not ocean[nr][nc]:
                        # print(r,c,nr,nc)
                        ocean[nr][nc] = True
                        queue.append((nr,nc))
                        # print(queue)
                        # print(pacific)
        
        bfs(queue_pacific,pacific)
        bfs(queue_atlantic,atlantic)

        # print(pacific)
        # print(atlantic)

        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r,c])

        return result           

        