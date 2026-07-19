class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        /**
         * brute force :
         * for each ele -> i can find amount of water it holds
         * have max value -> relax max if we find greater amount of water
         * 
         * return max
         * 
         * o(n*n)
         * 
         * linear time:
         * 
         * have two pointers
         * 
         * while(fp<sp):
         *    currCap = Math.min(heights[fp],heights[sp]) * sp - fp;
         *    relax max => if(currCap > max);
         * 
         *    if(heights[fp]<heigths[sp]) fp++;
         *    sp--;
         */

        let left = 0;
        let right = heights.length - 1;
        let res = 0;

        while (left < right) {
            const containerLength = right - left;
            const area =
                containerLength * Math.min(heights[left], heights[right]);
            res = Math.max(res, area);
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return res;
    }
}
