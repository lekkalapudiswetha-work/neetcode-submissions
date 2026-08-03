class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum(nums) % 2:
        #     return False
        
        # def dfs(i,target):
        #     if i >= len(nums):
        #         return target == 0
            
        #     if target < 0:
        #         return False
            
        #     return dfs(i+1,target) or dfs(i+1,target-nums[i])
        
        # return dfs(0,sum(nums)//2)

        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total //2
        n = len(nums)
        dp = [[False] * (target+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1,target+1):
                if nums[i-1] <= j:
                    dp[i][j] = (dp[i-1][j] or dp[i-1][j-nums[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][target]
        