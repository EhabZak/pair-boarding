from typing import List
from typing import Optional, List
from collections import defaultdict, Counter


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def path_count(m,n):
            if m == 0 and n == 0: return 0
            elif m == 1 and n == 1: return 1

            return path_count(m-1,n) + path_count(m, n-1)
        return path_count(m,n)


'''
it starts finding the paths from the bottom because of the recursion and goes to  0,0 to find the paths
it can be 0,0 and target be m-1 , n-1 or it can be 1,1 and m and n when you draw the grid.
this solution didn't pass on leet code because it is too slow there is another dynamic programming solution that is better.
'''
m = 3
n = 2

solution = Solution()
output = solution.uniquePaths(m,n)
print(output)
