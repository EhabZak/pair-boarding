from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        if grid[0][0] ==1 or grid[rows-1][cols-1] == 1:
             return -1
        def inbound(r,c):
                rowInbound = 0 <= r < rows
                colInbound = 0 <= c < cols
                return rowInbound and colInbound

        queue = deque()
        queue.append((0,0,1))
        visited = set()
        visited.add((0,0))
        directions = ((1,0),(0,1),(-1,0),(0,-1),(1,1), (1,-1),(-1,1), (-1,-1))




        while (queue):
            r,c, level = queue.popleft()
            # base case
            if r == rows-1 and c == cols-1:
                return level

            for dir in directions:
                newRow = r + dir[0]
                newCol = c + dir[1]
                if inbound(newRow,newCol) and (newRow, newCol) not in visited and grid[newRow] [newCol] != 1:
                     queue.append((newRow,newCol,level+1))
                     visited.add((newRow,newCol))
        return -1




grid = [[0,0,0],[1,1,0],[1,1,0]] # 4
sol = Solution()
print(sol.shortestPathBinaryMatrix(grid))
