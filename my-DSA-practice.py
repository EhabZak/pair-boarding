from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows , cols = len(mat) , len(mat[0])
        directions = ((1,0),(0,1),(-1,0),(0,-1))


        def inbound(r,c):
            rowInbound = 0 <= r < rows
            colInbound = 0 <= c < cols

        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
            else:
                mat [r][c] == -1

        while queue:
            r,c = queue.popleft()

            for dir in directions:
                newRow = r + dir[0]
                newCol = c + dir[1]

                if not inbound(newRow,newCol) or mat[newRow][newCol] != -1: continue

                mat[newRow][newCol] = mat[r][c]+ 1
                queue.append((newRow,newCol))
        return mat



mat = [[0,0,0],[0,1,0],[0,0,0]]
sol = Solution()
print(sol.updateMatrix(mat))
