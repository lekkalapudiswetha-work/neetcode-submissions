class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return nums[0]
        
        if length == 2:
            return max(nums[0],nums[1])

        dp_FH = [0] * (length-1)
        dp_FH[0] = nums[0]
        if length > 1: dp_FH[1] = max(nums[0],nums[1])
        for i in range(2,length-1):
            dp_FH[i] = max(nums[i]+dp_FH[i-2],dp_FH[i-1])
        
        dp_LH = [0] * length
        dp_LH[0] = 0
        if length > 1: dp_LH[1] = nums[1]
        for i in range(2,length):
            dp_LH[i] = max(nums[i]+dp_LH[i-2],dp_LH[i-1])

        return max(dp_FH[length-2] , dp_LH[length-1])

        