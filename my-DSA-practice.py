from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def backtrack(i):
            #base case
            if i >= len(nums):
                ans.append(subset.copy())
                return
            # to include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            # exclude
            backtrack(i+1)
        backtrack(0)
        return ans


nums = [1,2,3]
sol = Solution()
print(sol.subsets(nums))
