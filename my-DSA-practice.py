from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def fib(self, n: int, memo= {}) -> int:

        if n == 0: return 0
        if n == 1: return 1
        if n in memo: return memo[n]
        memo[n] = self.fib(n-1)+ self.fib(n-2)
        print (memo )
        print (memo[n] )
        return memo[n]


n = 5
solution = Solution()
output = solution.fib(n)
print(output)
