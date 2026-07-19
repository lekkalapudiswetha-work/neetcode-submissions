class Solution {
    /**
     * @param {number} m
     * @param {number} n
     * @return {number}
     */
    uniquePaths(m, n) {
        const dp = Array.from(Array(m),()=>Array(n).fill(1));
        //dp[m-1][n-1] = 1;
        console.log(dp);
        
        //for(let i = n -1;i)
        
        for(let i = m-2 ; i>=0;i--){
            for(let j = n-2; j>=0 ; j--){
                if(i === m-1 && j === n-1) dp[i][j] = 1;
                dp[i][j] = dp[i+1][j] + dp[i][j+1];
            }
            console.log(dp);
        }
        return dp[0][0];
    }
}