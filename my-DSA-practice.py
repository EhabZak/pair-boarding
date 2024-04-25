from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         dp = [0] + [amount + 1] * amount

#         for coin in coins:
#             for i in range(coin, amount + 1):
#                 dp[i] = min(dp[i], dp[i - coin] + 1)

#         return -1 if dp[amount] == amount + 1 else dp[amount]
        # def dfs ( rem, memo):
        #     if rem == 0: return 0
        #     if rem in memo: return memo[rem]

        #     memo[rem] = float('inf')

        #     for coin in coins:
        #         if rem-coin >= 0:
        #             memo[rem]= min (memo[rem], dfs(rem-coin, memo)+1)
        #     return memo[rem]

        # memo = defaultdict(int)
        # result = dfs(amount,memo)
        # return result if result != float('inf') else -1

    #! faster solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1) # amount+1 to represent infinity
        # print (dp)
        dp[0] = 0
        for index in range(amount+1):
            for coin in coins:
                if coin <= index:
                    dp[index] = min(dp[index] , dp[index-coin] + 1 )
        return dp[amount] if dp[amount]!=amount+1 else -1



coins = [1,2,5] #3
# amount = 11
amount = 6
solution = Solution()
output = solution.coinChange(coins, amount)
print(output)
