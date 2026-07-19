class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        /**
         * two pointers, set between distance of k
         * iterate till second pointer becomes n-1
         * for each set of k , find max
         * 
         */

        let p1 = 0;
        let p2 = k-1;
        let result =[];

        if(k === 1) return nums;

        const max = (nums,i,j)=>{
            return nums.slice(i,j+1).reduce((a,b)=>Math.max(a,b));
        }

        while(p2 < nums.length){
            result.push(max(nums,p1,p2));
            p1++;
            p2++;
        }

        return result;


    }
}
