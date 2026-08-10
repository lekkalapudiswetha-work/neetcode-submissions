class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1
        # dp = {}
        
        # def dfs(i,a):
        #     if a == 0:
        #         return 1
            
        #     if i >= n:
        #         return 0
            
        #     if (i,a) in dp:
        #         return dp[(i,a)]
            
        #     res = 0
            
        #     if a >= coins[i]:
        #         res = dfs(i+1,a)
        #         res += dfs(i,a-coins[i])
        #     dp[(i,a)] = res
        #     return res
        
        # return dfs(0,amount)

        for i in range(n):
            for amount in range(1,amount+1):
                dp[amount] += dp[amount-coins[i]] if coins[i] <= amount else 0
        
        return dp[amount]

        
        
        