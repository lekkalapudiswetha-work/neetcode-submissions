class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for str in strs:
            key = "".join(sorted(str))
            group.setdefault(key,[]).append(str)
        
        return list(group.values())
        