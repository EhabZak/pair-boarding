from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def climbStairs(self, n: int, memo ={}) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n in memo: return memo[n]

        memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return memo[n]





n = 3

solution = Solution()
output = solution.climbStairs(n)
print(output)
