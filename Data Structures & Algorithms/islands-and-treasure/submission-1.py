class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        distance = 0

        directions = [
            [1,0],[-1,0],[0,1],[0,-1]
        ]

        while queue:
            distance += 1
            # print(queue,distance)
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr , dc in directions: 
                    nr = r+dr
                    nc = c+dc
                    # print(nr,nc, 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647)
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                        # print(nr,nc)
                        grid[nr][nc] = distance
                        queue.append((nr,nc))



