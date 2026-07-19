class Solution {
    /**
     * @param {string} text1
     * @param {string} text2
     * @return {number}
     */
    longestCommonSubsequence(text1, text2) {
        /**
         * Base case :
         * if both are equal :
         *      increment length by 1 and find the max of remaining of both texts
         * else:
         *      find max between choosing letter from text 1 or text 2
         *
         */

        
        let lengthSubSequence = Array.from(Array(text1.length+1),()=>Array(text2.length+1).fill(0));
        //console.log(lengthSubSequence);
       
       for(let i = text1.length-1 ; i>=0 ; i--){
           for(let j = text2.length-1 ; j>=0 ; j--){
            //console.log(i+1,j+1);
               if(text1[i]===text2[j]){
                   lengthSubSequence[i][j] = 1 + lengthSubSequence[i+1][j+1];
               }else{
                   lengthSubSequence[i][j] = Math.max(lengthSubSequence[i+1][j],lengthSubSequence[i][j+1]);
               }
           }
       }
       
       return lengthSubSequence[0][0];



    }
}
