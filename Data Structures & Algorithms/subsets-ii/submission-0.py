class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def backtrack(i,currCombi):
            if i == len(nums):
                result.append(currCombi.copy())
                return
            
            currCombi.append(nums[i])
            backtrack(i+1,currCombi)
            currCombi.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1,currCombi)
        
        backtrack(0,[])

        return result

        