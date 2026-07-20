class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        /**
         * for each element in array we have choice to insert element or not insert
         */

        let res = [];
        //let subset = [];

        const dfs = (i,subset)=>{
            if(i>=nums.length){
                res.push([...subset]);
                return;
            }
            subset.push(nums[i]);
            dfs(i+1,subset);
            subset.pop();
            dfs(i+1,subset);
        }

        dfs(0,[]);

        return res;

    }
}
