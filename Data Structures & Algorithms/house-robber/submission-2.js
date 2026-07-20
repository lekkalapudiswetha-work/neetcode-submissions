class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        // let n = nums.length;
        // if(n===1) return nums[0];
        // for(let i = 2;i<nums.length;i++){
        //     nums[i] = nums[i] + nums[i-2];
        // }
        // return Math.max(nums[nums.length-1],nums[nums.length-2]);
        let rob1 = 0;
            let rob2 = 0;

        for (const n of nums) {
            const temp = Math.max(n + rob1, rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        return rob2;
    }
    
}
