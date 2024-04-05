from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        # dfs helper function an three base cases
        # out of bound, in viisted , if value is == 0
        #in bound helper function
        # directions check
        # position check in visited

        # coordinates and do the thing

        largestIsland = 0
        visited = set()

        for r in range(rows):
            for c in range(cols):
                largestIsland = max(largestIsland, dfs(r,c))

        return largestIsland




        # return the largest island










grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

sol = Solution()
print(sol.maxAreaOfIsland(grid))
