class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {

        let maxValue = prices[prices.length-1];
        let result = 0;

        for(let i = prices.length-1;i>=0;i--){
            if(prices[i]<maxValue){
                result = Math.max(result,maxValue-prices[i]);
            }else{
                maxValue = prices[i];
            }
        }

        return result;
    }
}
