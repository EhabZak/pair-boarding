from typing import List
from typing import Optional, List
from collections import defaultdict, Counter

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len (matrix[0])

        top, bottom = 0 , rows-1

        while top <= bottom:
            row = top + (bottom-top)//2

            if target > matrix[row][cols-1]:
                top = row+1
            elif target < matrix[row][0]:
                bottom = row-1
            else:
                break

        row = top + (bottom- top)//2
        left,right = 0 , cols-1

        while left<= right:
            mid = left + (right-left)//2
            if target > matrix [row] [mid]:
                left = mid + 1
            elif target < matrix [row] [mid]:
                right = mid -1
            else:
                return True
        return False








# matrix = [[1],[3]]
matrix = [[1]]
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 2
solution = Solution()
output = solution.searchMatrix(matrix,target)
print(output)
