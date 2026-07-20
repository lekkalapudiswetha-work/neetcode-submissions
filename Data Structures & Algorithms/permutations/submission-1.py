class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)

        def backtrack(currCombi):
            if len(currCombi) == len(nums):
                result.append(currCombi.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    currCombi.append(nums[i])
                    used[i] = True
                    backtrack(currCombi)
                    currCombi.pop()
                    used[i] = False

        backtrack([])

        return result

            
            

            

        