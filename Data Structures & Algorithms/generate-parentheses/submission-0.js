class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {

        let res = [];

        const validParenthesis = (openCount,closeCount,sequence)=>{
            if(openCount === n && closeCount === n){
                res.push(sequence);
                return;
            }

            if(openCount !== n){
                validParenthesis(openCount+1,closeCount,sequence+'(');
            }

            if(closeCount < openCount){
                validParenthesis(openCount,closeCount+1,sequence+')');
            }

        }

        validParenthesis(0,0,'');
        return res;
    }
}
