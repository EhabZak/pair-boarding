from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1 for _ in range(n)] for _ in range(m)] # creates a 2D list (or matrix) # [[1, 1], [1, 1], [1, 1]] representing rows and cols
        # print (table) # [[1, 1], [1, 2], [1, 3]] # first row and the first column are already initialized
        for i in range(1,m): #stop value is excluded
            for j in range(1,n):
                table[i][j] = table[i-1][j]+ table[i][j-1]
                # Each cell stores the number of unique paths to reach it by summing up the number of
                #paths from the cell above and the cell to the left.
                print ('i is ===',i)
                print ('j is ********',j)
                print (table[i][j])
        print (table)
        return table[m-1][n-1]



m = 3
n = 7
# n = 7

solution = Solution()
output = solution.uniquePaths(m,n)
print(output)
