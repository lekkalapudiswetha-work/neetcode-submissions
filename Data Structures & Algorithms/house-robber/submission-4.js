class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        let n = nums.length;
        if(n===1) return nums[0];
        let maxArr = [];
        nums[0] = nums[0];
        nums[1] = Math.max(nums[0],nums[1]);
        for(let i = 2 ;i < nums.length ; i++){
            nums[i]=Math.max(nums[i]+nums[i-2],nums[i-1]);
        }
        return nums[nums.length-1];
    }
    
}
