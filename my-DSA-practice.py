from typing import List
from typing import Optional, List
from collections import defaultdict, Counter


from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged


# Example usage
nums = [5, 1, 1, 2, 0, 0]
solution = Solution()
output = solution.sortArray(nums)
print(output)

