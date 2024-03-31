from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] =='1':
                    count+=1
                    dfs(r,c)
        return count














# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
print(sol.numIslands(grid))
