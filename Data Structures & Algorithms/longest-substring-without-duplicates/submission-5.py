class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen = set()
        right = 0

        while right<len(s):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
            seen.add(s[right])
            currLength = right-left + 1
            max_length = max(max_length,currLength)
            right+=1
        
        return max_length


        