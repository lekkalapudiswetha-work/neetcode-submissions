class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    lengthOfLIS(nums) {
        /**
         * subProblem : find LIS[i] = LIS[i:]
         * relation:
         * include i in subsequence and calculate
         * LIS[i] = max(LIS[i],1+LIS[j]) Where, nums[j]>nums[i] , i<j<nums.length
         * max LIS[i];
         */
        let n = nums.length;
        let LIS = Array(n).fill(1);
        //console.log(LIS);
       //console.log(n-2,n-2+1);
        for(let i=n-2;i>=0; i--){
            for(let j=i+1; j<n ; j++){
                if(nums[j]>nums[i]){
                    LIS[i] = Math.max(LIS[i],1+LIS[j]);
                }
            }
        }
        return LIS.reduce((a,b) => Math.max(a,b) , -Infinity);
    }
}
