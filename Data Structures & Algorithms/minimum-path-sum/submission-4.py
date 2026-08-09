class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # dp = [[0] * cols for _ in range(rows)]

        # dp[0][0] = grid[0][0]

        # for i in range(rows):
        #     for j in range(cols):
        #         if i ==0 and j==0:
        #             continue
        #         elif i == 0:
        #             dp[i][j] = grid[i][j] + dp[i][j-1]
        #         elif j == 0:
        #             dp[i][j] = grid[i][j] + dp[i-1][j]
        #         else:
        #             dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        
        # #print(dp)
        
        # return dp[rows-1][cols-1]

        dp = [float('inf')] * (cols+1)
        dp[cols-1] = 0

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                dp[j] = grid[i][j] + min(dp[j],dp[j+1])
        
        return dp[0]