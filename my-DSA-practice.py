from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        # dfs helper function an three base cases
        def dfs(r,c):
            if not inbound(r,c) or grid[r][c] == 0:
                return 0
            pos = (r,c)
            if pos in visited:
                return 0

            visited.add(pos)
            size = 1

            directions = ((0,1),(0,-1),(1,0),(-1,0))
            for dir in directions:
                realRow = r + dir[0]
                realCol = c + dir[1]
                size += dfs(realRow, realCol)
            return size




        def inbound(r,c):
            rowIn = 0 <= r < rows
            colIn = 0 <= c < cols
            return rowIn and colIn




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
