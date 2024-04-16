from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # rows,cols = len(mat), len(mat[0])
        # directions = ((1,0),(0,1),(-1,0),(0,-1))

        # def inbound(r,c):
        #     rowInbound = 0 <= r < rows
        #     colInbound = 0 <= c < cols
        #     return rowInbound and colInbound
        # queue = deque()
        # for r in range(rows):
        #     for c in range(cols):
        #         if mat[r][c] ==0 :
        #             queue.append((r,c))
        #         else:
        #             mat[r][c] = -1
        # while queue:
        #     r,c = queue.popleft()

        #     for dir in directions:
        #         newRow = r + dir[0]
        #         newCol = c + dir[1]

        #         if not inbound(newRow, newCol) or mat[newRow][newCol] != -1: continue
        #         mat [newRow][newCol] = mat[r][c] +1
        #         queue.append((newRow,newCol))
        # return mat
        rows,cols = len(mat), len(mat[0])
        directions = ((0,1),(1,0),(0,-1),(-1,0))

        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    print ('mat====>', mat)
                    mat[r][c] = min(top, left) + 1
                    print (min(top, left))

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
        return mat



mat = [[0,0,0],[0,1,0],[1,1,1]]
# mat = [[0,0,0],[0,1,0],[0,0,0]]
sol = Solution()
print(sol.updateMatrix(mat))
