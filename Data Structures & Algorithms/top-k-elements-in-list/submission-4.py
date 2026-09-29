class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]

        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for num,count in freq.items():
            buckets[count].append(num)
        
        result = []

        for count in range(len(nums),0,-1):
            for num in buckets[count]:
                result.append(num)
            
            if len(result) == k:
                return result

        