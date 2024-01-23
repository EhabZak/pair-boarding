from typing import List
from typing import Optional, List
from collections import defaultdict, Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        frequencies = defaultdict(int)

        def _dfs(node):
            if not node:
                return

            frequencies[node.val] += 1
            _dfs(node.left)
            _dfs(node.right)

        _dfs(root)

        max_freq = max(frequencies.values())
        res = []

        for node in frequencies:
            if frequencies[node] == max_freq:
                res.append(node)
        return res
'''
    1
     \
      2
     /
    2
'''

root = TreeNode(1, None, TreeNode(2, TreeNode(2), None))

# Create a bigger binary tree
# root = TreeNode(5,
                # left=TreeNode(3, TreeNode(1), TreeNode(5)),
                # right=TreeNode(8, TreeNode(7), TreeNode(9)))
'''
        5
       / \
      3   8
     /|   |\
    1 5   7 9

'''
# Create an instance of the Solution class
solution = Solution()

# Call the findMode method and print the result
output = solution.findMode(root)
print(output)
