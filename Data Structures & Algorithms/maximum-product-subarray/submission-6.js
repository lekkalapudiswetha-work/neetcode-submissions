class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxProduct(nums) {
        /**
         * subproblem :
         * for each a[i:] -> find min and max.
         * relation:
         * currMax=Max(a[i],a[i]*currMax,a[i]*currMin);
         * currMin = Min(a[i],a[i]*currMin,a[i]*currmax);
         * 
         * max = max(max,currMax);
         */

        let currMax =1 , currMin =1 , res = -Infinity;

        for(const a of nums){
            let temp = a*currMax;
            currMax = Math.max(Math.max(a*currMax,a*currMin),a);
            currMin = Math.min(Math.min(temp,a*currMin),a);
            res = Math.max(currMax,res);

        }
        return res;
    }
}
