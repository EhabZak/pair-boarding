from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        left = 0
        for right in range(len(nums)):
            if left - right >k:
                window.discard(nums[left])
                left +=1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False 




nums = [1,2,3,1] # True
k = 3

# nums = [11,0,11,11] # True
# k = 1

# nums = [1,2,3,1,2,3] # False
# k = 2

solution = Solution()
output = solution.containsNearbyDuplicate(nums, k)
print(output)
