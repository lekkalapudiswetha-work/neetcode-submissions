class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        maxi_island = 0

        def dfs(r,c):
            if 0<= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r,c) not in visited:
                visited.add((r,c))
                return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))
            else:
                return 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxi_island = max(maxi_island,dfs(r,c))
        
        return maxi_island
        
