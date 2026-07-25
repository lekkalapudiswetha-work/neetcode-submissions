class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        dp = [-1] * (amount+1)

        for i in range(1,amount+1):
            currMin = float("inf")
            for j in range(len(coins)):
                if i - coins[j] == 0:
                    currMin = 1
                if i - coins[j] > 0 and dp[i - coins[j]] != -1:
                    currMin = min(currMin,1+dp[i - coins[j]])
            
            if currMin != float("inf"):
                dp[i] = currMin
        
        return dp[amount]

        