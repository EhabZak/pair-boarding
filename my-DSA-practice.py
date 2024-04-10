from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(r,c,visited,prevHeight):
            if not inbound(r,c) or (r,c) in visited or heights[r][c]< prevHeight:
                return

            visited.add((r,c))

            directions = ((0,1), (0,-1),(1,0),(-1,0))
            for dir in directions:
                newRow = r +dir[0]
                newCol = c + dir[1]
                dfs(newRow, newCol, visited,heights[r][c])


        def inbound(r,c):
            rowIn = 0 <= r < rows
            colIn = 0 <= c < cols
            return rowIn and colIn


        res = []
        pacific = set()
        atlantic = set()

        for c in range(cols):
            # north side
            dfs(0,c,pacific,heights[0][c])

            # south side
            dfs(rows-1,c,atlantic,heights[rows-1][c])

        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])

            dfs(r,cols-1,atlantic,heights[r][cols-1])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])




        return res




heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
sol = Solution()
print(sol.pacificAtlantic(heights))
