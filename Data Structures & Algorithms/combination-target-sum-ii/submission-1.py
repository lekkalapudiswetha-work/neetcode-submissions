class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def backtrack(i,currSum,currCombi):
            if currSum == target:
                result.append(currCombi.copy())
                return
            
            if target < currSum or i >= len(candidates):
                return
            
            currCombi.append(candidates[i])
            backtrack(i+1,currSum+candidates[i],currCombi)
            currCombi.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1,currSum,currCombi)
        
        backtrack(0,0,[])

        return result
        