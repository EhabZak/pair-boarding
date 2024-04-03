from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])

        # dfs helper function and base cases
        def dfs(r,c):
            if not inbound(r,c) or grid[r][c] == 0:
                return 0

        # check position in visited
            pos = (r,c)
            if pos in visited:
                return 0
            size = 1

            visited.add(pos)

        # check direction
            directions = ((0,1),(0,-1),(1,0),(-1,0))
            for dir in directions:
                newR = r + dir[0]
                newC = c + dir[1]
                size += dfs(newR,newC)

        # return what you size from dfs
            return size

        # check if inbound helper function

        def inbound(r,c):
            rowIn = 0 <= r < rows
            colIn = 0 <= c < cols
            return rowIn and colIn




        # iterate over grid for each cell coordinates and find max
        largestIsland = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                largestIsland = max( largestIsland, dfs(r,c))

        return largestIsland










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
