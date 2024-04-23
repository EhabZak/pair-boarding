from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def fib(self, n: int, mono = {}) -> int:

        if n == 0: return 0
        if n == 1: return 1
        if n in mono: return mono[n]

        mono[n] = self.fib(n-1)+ self.fib(n-2)
        return mono[n]




n = 5
solution = Solution()
output = solution.fib(n)
print(output)
