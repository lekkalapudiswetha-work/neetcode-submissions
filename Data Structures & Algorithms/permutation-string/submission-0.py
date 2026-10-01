class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        s2_freq = {}

        if len(s2) < len(s1):
            return False

        for char in s1:
            s1_freq[char] = s1_freq.get(char,0) + 1
        
        left = 0
        right = 0

        for right in range(len(s2)):
            s2_freq[s2[right]] = s2_freq.get(s2[right],0) +1

            if right - left + 1 > len(s1):
                s2_freq[s2[left]] -=1
                if s2_freq[s2[left]] == 0:
                    del s2_freq[s2[left]]
                left += 1
            
            if s1_freq == s2_freq:
                return True
            
            
            
        
        return False







        
        