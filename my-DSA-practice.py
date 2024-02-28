from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q: return False
        if p and not q: return False
        if not p and not q: return True
        if p != q: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


## example 1
# p1 = TreeNode(1)
# p1.left = TreeNode(2)
# p1.right = TreeNode(3)

# q1 = TreeNode(1)
# q1.left = TreeNode(2)
# q1.right = TreeNode(3)



    # Example 3
p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(1)

q1 = TreeNode(1)
q1.left = TreeNode(1)
q1.right = TreeNode(2)

solution = Solution()
print (solution.isSameTree(p1, q1))
