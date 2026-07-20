class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def backtrack(i,currLen,currCombi):

            if currLen == k:
                result.append(currCombi.copy())
                return
            
            if i>n:
                return
            
            currCombi.append(i)
            backtrack(i+1,currLen+1,currCombi)
            currCombi.pop()
            backtrack(i+1,currLen,currCombi)

        backtrack(1,0,[])
        return result

        