class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        left_sum = [1] * length_nums
        right_sum = [1] * length_nums
        output = [0] * length_nums

        for i in range(1,length_nums):
            left_sum[i] = left_sum[i-1] * nums[i-1]
        
        for j in range(length_nums-2,-1,-1):
            right_sum[j] = right_sum[j+1] * nums[j+1]
        
        for idx in range(0,length_nums):
            output[idx] = left_sum[idx] * right_sum[idx]

        return output



            
        