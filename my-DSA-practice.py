from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class TreeNode:
    def __init__(self, val = 0, left= None, right= None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pot(self, root):
        if root is None: return []

        left = self.pot(root.left)
        right = self.pot(root.right)
        return left+right+ [root.val]

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Instantiate the Solution class
sol = Solution()

# Test the inorderTraversal method
result = sol.pot(root)
print(result)
