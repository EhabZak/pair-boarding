from typing import List
from typing import Optional, List
from collections import defaultdict, Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            next1 = list1.next
            list1.next = self.mergeTwoLists(next1,list2)

        else:
            next2 = list2.next
            







list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Instantiate Solution class
sol = Solution()

# Call mergeTwoLists method
merged_list = sol.mergeTwoLists(list1, list2)
while merged_list is not None:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
