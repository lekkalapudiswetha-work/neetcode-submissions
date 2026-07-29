class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * len(nums)

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if j <= n-1 and nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
        
        maxi = 0
        for i in range(n):
            maxi = max(maxi,dp[i])
        
        return maxi
