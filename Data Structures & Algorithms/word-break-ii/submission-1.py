class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []

        def checkWord(i,j):
            if s[i:j+1] in wordDict:
                return True
            return False

        def backtrack(i,currString):
            if i >= len(s):
                result.append(currString.strip())
                return
            
            for j in range(i,len(s)):
                if checkWord(i,j):
                    backtrack(j+1,currString+s[i:j+1] + ' ')
        
        backtrack(0,'')
        return result
        