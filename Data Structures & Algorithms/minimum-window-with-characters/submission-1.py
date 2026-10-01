class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        formed = 0
        required = 0
        l = 0
        r=0
        start = 0
        min_length = len(s) + 1
        
        for char in t:
            need[char] = need.get(char,0) + 1
        
        required = len(need)

        for r in range(len(s)):
            if s[r] in need:
                window[s[r]] = window.get(s[r],0) + 1
                if need[s[r]] == window[s[r]]:
                    formed += 1
            
            while formed == required:
                if min_length > r-l+1:
                    min_length = r-l+1
                    start = l
                if s[l] in window:
                    if window[s[l]] == need[s[l]]:
                        formed -= 1
                    window[s[l]] -= 1
                l += 1
        
        return s[start:start+min_length] if min_length != len(s)+1 else ''


        

        