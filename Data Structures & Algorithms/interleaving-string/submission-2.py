class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s3) != len(s1) + len(s2):
            return False
        def backtrack(i,j):
            if (i+j) == len(s3):
                return i == len(s1) and j == len(s2)
            if (i,j) in dp:
                return dp[(i,j)]
            res = False
            if i < len(s1) and s1[i] == s3[i+j]:
                res = backtrack(i+1,j)
            if j < len(s2) and s2[j] == s3[i+j]:
                res = backtrack(i,j+1)
            
            dp[(i,j)] = res
            return res
        
        return backtrack(0,0)
            
        