class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []

        def checkWord(i,j):
            if s[i:j+1] in wordDict:
                return True
            return False

        def backtrack(i,curr):
            if i >= len(s):
                result.append(' '.join(curr))
                return
            
            for j in range(i,len(s)):
                if checkWord(i,j):
                    curr.append(s[i:j+1])
                    backtrack(j+1,curr)
                    curr.pop()
        
        backtrack(0,[])
        return result
        