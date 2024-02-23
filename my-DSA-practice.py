from typing import List
from typing import Optional, List
from collections import defaultdict, Counter


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        output = []
        while queue:
            # shift out of the queue
            node = queue.popleft()
            if node:
                output.append(node.val)
                #adding children to the queue
                queue.append(node.left)
                queue.append(node.right)
        return output

