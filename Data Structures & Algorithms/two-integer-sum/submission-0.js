class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let map = new Map();
        for(let i in nums){
            if(map.has(target-nums[i])){
                return [Number(map.get(target-nums[i])),Number(i)];
            }
            map.set(nums[i],i);
        }
        return -1;
    }
}
