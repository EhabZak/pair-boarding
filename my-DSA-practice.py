from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if inbound(r,c) or grid[r][c] == 0:
                return 0


            pos = (r,c)
            if pos in visited:
                return 0
            size = 1
            visited.add(pos)

            directions = ((0,1),(1,0),(0,-1),(-1,0))

            for dir in directions:
                realRow = r +dir[0]
                realCol = c + dir[1]
                size += dfs(realRow, realCol)
            

            return size


        def inbound(r,c):
            rowInbound = 0 < r < rows
            colInbound = 0 < c < cols
            return rowInbound and colInbound


        largestIsland = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    largestIsland = max(largestIsland, dfs(r,c))


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
