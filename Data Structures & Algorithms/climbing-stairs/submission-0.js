class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        if(n === 1 || n === 2) return n;
        return this.climbStairs(n-1)+this.climbStairs(n-2);
    }
}
