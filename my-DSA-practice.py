from typing import List
from typing import Optional, List
from collections import defaultdict, Counter


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        def _helper(head, prev):
        #    print('head', head.value if head else None)
           if head is None:
               return prev

           next = head.next
        #    print('next', next.value if next else None)
           head.next = prev
        #    print ('head.next',head.next.value if head.next else None)
           return _helper(next,head)
        return _helper(head,prev)

# Convert the input list to a linked list
head_values = [1, 2, 3, 4, 5]
head = ListNode(head_values[0])
current_node = head
for value in head_values[1:]:
    current_node.next = ListNode(value)
    current_node = current_node.next

# Create an instance of Solution
solution = Solution()

# Test the reverseList method
reversed_head = solution.reverseList(head)

# Print the reversed linked list values
while reversed_head:
    print(reversed_head.value, end=" ")
    reversed_head = reversed_head.next
