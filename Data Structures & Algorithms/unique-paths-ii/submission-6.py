class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for j in range(1,cols):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
        
        for i in range(1,rows):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0

        for i in range(1,rows):
            for j in range(1,cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        
        return dp[rows-1][cols-1]