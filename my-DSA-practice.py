from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(rem,memo):
            if rem == 0: return 0
            if rem in memo: return memo[rem]

            memo[rem]= float("inf")
            print (memo)

            for coin in coins:
                print('coin is =',coin)
                if rem - coin >= 0:
                    memo[rem] = min (memo[rem], dfs(rem - coin, memo) +1)
                    print (memo)
            return memo[rem]


        memo = defaultdict(int)
        print (memo)
        result = dfs(amount, memo)
        return result if result != float("inf") else -1


coins = [1,2,5] #3
# amount = 11
amount = 6
solution = Solution()
output = solution.coinChange(coins, amount)
print(output)

