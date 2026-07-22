class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        maxLen = 0
        map = {}

        while r < len(s):
            if s[r] in map:
                l = max(l,map[s[r]]+1)
            map[s[r]] = r
            maxLen = max(maxLen,r-l+1)
            r+=1    
        
        return maxLen