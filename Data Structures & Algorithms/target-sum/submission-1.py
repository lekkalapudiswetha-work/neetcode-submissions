class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0
        dp = {}

        def dfs(i,sum):
            if i == n:
                return 1 if sum == target else 0
            
            if (i,sum) in dp:
                return dp[(i,sum)]
            
            dp[(i,sum)] = (dfs(i+1,sum+nums[i]) + dfs(i+1,sum-nums[i]))

            return dp[(i,sum)]
    
        return dfs(0,0)
        