class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return sorted(s) == sorted(t)

        # count_s, count_t = {}, {}
        # for i in range(len(s)):
        #     count_s[s[i]] = 1 + count_s.get(s[i],0)
        #     count_t[t[i]] = 1 + count_t.get(t[i],0)
        
        # return count_s == count_t

        check = [0] * 26

        for i in range(len(s)):
            check[ord(s[i]) - ord('a')] += 1
            check[ord(t[i]) - ord('a')] -= 1
        
        for val in check:
            if val != 0:
                return False
        
        return True

        