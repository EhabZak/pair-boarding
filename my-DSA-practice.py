from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #base cases
        def dfs(row,col):
            if not inBound(row,col):
                return False
            pos = f'{row},{col}'

            if pos in visited:
                return False
            if grid[row][col] == '0':
                return False
            visited.add(pos)

            directions = ((1,0),(0,1), (-1,0),(0,-1))
            for dir in directions:
                newRow = row+ dir[0]
                newCol = col + dir[1]
                dfs(newRow, newCol)
            return True


        def inBound(row,col):
            rowInbound = 0 <= row and row < len(grid)
            colInbound = 0 <= col and col < len(grid[0])
            return rowInbound and colInbound

        count = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if dfs(row,col):
                    count += 1

        return count












grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
sol = Solution()
print(sol.numIslands(grid))
