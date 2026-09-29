class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        output = [1] * length_nums

        for i in range(1,length_nums):
            output[i] = output[i-1] * nums[i-1]
        
        
        right_product = 1
        
        for j in range(length_nums-1,-1,-1):
            output[j] *= right_product
            right_product *= nums[j]

        return output



            
        