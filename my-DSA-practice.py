from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def fib(self, n: int, mono = {}) -> int:


        if n ==1: return 1
        elif n == 0: return 0
        else:
            x = [0,1]
            y = 2

            while y < n:
                x.append(x[y-1]+x[y-2])
                y +=1
            return x[n-1]+x[n-2]







n = 5
solution = Solution()
output = solution.fib(n)
print(output)
