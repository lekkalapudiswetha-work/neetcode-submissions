class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        let n = nums.length;
        if(n===1) return nums[0];
        let maxArr = [];
        maxArr[0] = nums[0];
        maxArr[1] = Math.max(nums[0],nums[1]);
        for(let i = 2 ;i < nums.length ; i++){
            maxArr[i]=Math.max(nums[i]+maxArr[i-2],maxArr[i-1]);
        }
        return maxArr[nums.length-1];
    }
    
}
