class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(openCount,closeCount,curr):
            if openCount == n and closeCount == n:
                result.append(curr)
                return
            
            if openCount > n or closeCount > n:
                return
            
            if closeCount < openCount :
                backtrack(openCount,closeCount+1,curr+')')
            
            backtrack(openCount+1,closeCount,curr+'(')
        
        backtrack(0,0,'')
        return result


        
        
        