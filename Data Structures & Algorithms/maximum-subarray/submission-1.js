class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        /**
         * SubProblem : s[i:] max sum
         * relation :
         *    currSum = nums[i]+currSum;
         *    max = math.max(max,currSum);
         */

        let currSum = 0;
        let max = -Infinity;

        for(let i = nums.length-1 ; i>-1;i--){
            currSum = Math.max(currSum+nums[i],nums[i]);
            max = Math.max(max,currSum);
        }
        return max;
    }
}
