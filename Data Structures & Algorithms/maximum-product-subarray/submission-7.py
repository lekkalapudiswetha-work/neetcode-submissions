class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        result = nums[0]

        for i in range(1,len(nums)):
            num = nums[i]

            previous_max = maxi
            previous_min = mini

            maxi = max(num, previous_max * num, previous_min * num)
            mini = min(previous_max * num , previous_min * num , num)
        
            result = max(result,maxi)
        
        return result
