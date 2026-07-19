class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        let n = nums.length;
        if(n === 1) return nums[0];
        let maxFirst = [];
        let maxLast = [];
        maxFirst[0] = nums[0];
        maxFirst[1] = Math.max(nums[0],nums[1]);
        //maxFirst[n-1] = 0;
        maxLast[0] = 0;
        maxLast[1] = nums[1];
        for(let i=2; i<n-1;i++){
            maxFirst[i]=Math.max(nums[i]+maxFirst[i-2],maxFirst[i-1]);
        }
        for(let i=2;i<n;i++){
            maxLast[i]=Math.max(nums[i]+maxLast[i-2],maxLast[i-1]);
        }
        console.log(maxFirst);
        console.log(maxLast);
        return Math.max(maxFirst[n-2],maxLast[n-1]);

    }
}
