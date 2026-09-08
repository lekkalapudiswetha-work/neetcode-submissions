class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = map.get(num,0)+1
        
        count = len(nums)/2

        for num,currcount in map.items():
            if currcount > count:
                return num
        
        return 0

        