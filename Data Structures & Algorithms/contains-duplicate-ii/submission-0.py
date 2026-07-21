class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        while i <= len(nums):
            maxRange = min(len(nums),i+k+1)
            for j in range(i+1,maxRange):
                if j <= len(nums) and nums[i] == nums[j]:
                    return True
            i+=1
        
        return False