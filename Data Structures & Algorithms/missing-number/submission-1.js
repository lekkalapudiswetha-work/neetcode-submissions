class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    missingNumber(nums) {
        /**
         * iterate through all the nums array and check if nums[i-1]=nums[i] - 1
         * if not return nums[i]-1;
         *         
         *  
         * */

         let sum =0;
         let n = nums.length;
        for(let i = n-1;i>=0;i--){
            sum+=nums[i];
        }
        
        let requiredSum = ((n)*(n+1))/2;
        return requiredSum-sum;
    }
}
