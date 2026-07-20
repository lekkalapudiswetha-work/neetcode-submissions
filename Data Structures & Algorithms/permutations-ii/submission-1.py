class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(currCombi):
            if len(currCombi) == len(nums):
                result.append(currCombi.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                currCombi.append(nums[i])
                used[i] = True
                backtrack(currCombi)
                currCombi.pop()
                used[i]=False
                    

        backtrack([])
        return result
        