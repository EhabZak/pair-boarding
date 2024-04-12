from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        





grid = [[2,1,1],[1,1,0],[0,1,1]] # 4
grid = [[2,1,1],[2,1,0],[0,1,1]] # 3 # it takes them in pairs cause there are more than one starting node here

sol = Solution()
print(sol.orangesRotting(grid))
