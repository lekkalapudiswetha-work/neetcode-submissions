class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for idx,num in enumerate(nums):
            rem = target - num
            if rem in dict1:
                return [dict1[rem],idx]
            
            dict1[num] = idx


        
        