from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows ,cols = len(grid), len(grid[0])

        queue = deque()
        freshOranges = 0
        time = 0

        def inbound(r,c):
            rowInbound = 0 <= r < rows
            colInbound = 0 <= c < cols
            return rowInbound and colInbound

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshOranges +=1
                elif grid[r][c] ==2:
                    queue.append((r,c,0))

        directions = ((1,0),(0,1),(-1,0),(0,-1))
        while queue:
            r,c,level = queue.popleft()
            time  = level
            for dir in directions:
                newRow = r + dir[0]
                newCol = c + dir[1]
                if inbound(newRow,newCol) and grid[newRow][newCol] == 1:
                    queue.append((newRow,newCol,level+1))
                    grid[newRow][newCol] = 2
                    freshOranges -=1
        return time if freshOranges == 0  else -1














grid = [[2,1,1],[1,1,0],[0,1,1]] # 4
grid = [[2,1,1],[2,1,0],[0,1,1]] # 3 # it takes them in pairs cause there are more than one starting node here

sol = Solution()
print(sol.orangesRotting(grid))
