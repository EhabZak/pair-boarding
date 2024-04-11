from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        






grid = [[0,0,0],[1,1,0],[1,1,0]] # 4
sol = Solution()
print(sol.shortestPathBinaryMatrix(grid))
