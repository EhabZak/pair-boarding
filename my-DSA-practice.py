from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def backtrack(r,c,i):
            #base cases
            if i == len(word):
                return True
            if not inbound(r,c) or  word[i] != board[r][c] or (r,c) in visited:
                return False

            # do the thing
            visited.add((r,c))

            #recursion
            res = (backtrack(r+1,c, i+1) or
                   backtrack(r-1,c, i+1) or
                   backtrack(r,c+1, i+1) or
                   backtrack(r,c-1, i+1))

            #backtrack

            visited.discard((r,c))

            return res

            # inbound
        def inbound(r,c):
            rowInbound = r >= 0 and r < ROWS
            colInbound = c >= 0 and c < COLS
            return rowInbound and colInbound


        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0):
                    return True
        return False



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
sol = Solution()
print(sol.exist(board, word))
