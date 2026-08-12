class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        visit = set()

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 1
            if (i,j) in visit:
                return 0

            visit.add((i,j))
            perim = dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            return perim

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r,c) 
        
        return 0
        