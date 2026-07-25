class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        if length > 1: dp[1] = max(nums[1],nums[0])
        for i in range(2,length):
            dp[i] = max(nums[i]+dp[i-2] , dp[i-1])
        
        return dp[length-1]
        