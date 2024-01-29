from typing import List
from typing import Optional, List
from collections import defaultdict, Counter

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums)-1

        while left <= right:
            mid = left+ (right-left)// 2
            if nums[mid] == target:
                return mid
            elif nums[mid]> target:
                right = mid-1
            else:
                left = mid + 1

        return -1





nums = [-1,0,3,5,9,12]

# target = 9
target = 12

output = Solution().search(nums,target)
print(output)
