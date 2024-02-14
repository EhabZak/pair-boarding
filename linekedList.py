import math
import os
import random
import re
import sys
import json
from typing import List
from typing import Optional, List
from collections import defaultdict, Counter


#! 1-to create a node
# class ListNode:
#     def __init__(self, value=0, next= None):
#         self.value = value
#         self.next = next

# nums = [13, 24, 34, 44, 54]
# head = ListNode(nums[0])
# current = head
# for number in nums[1:]:
#     current.next = ListNode(number)
#     current = current.next
# current = head
# while current:
#     print (current.value)
#     print (current.next.value if current.next else None)
#     current = current.next


# #! to create a node with lots of prints
# class ListNode:
#     def __init__(self, value=0, next= None):
#         self.value = value
#         self.next = next
# #! if you want to print the node as a string add this function
#     def __str__(self):
#         # Convert the ListNode instance to a string representation
#         return f"ListNode(value={self.value}, next={self.next})"
# #! if you want to print the node as a dictionary add this function
#     def to_dict(self):
#         if self.next is not None:
#             return {'value': self.value, 'next': self.next.to_dict()}
#         else:
#             return {'value': self.value, 'next': None}
# #! if you want to print the node as a linked list shape add this function
#     def print_linked_list(self):
#         current = self
#         while current:
#             print(current.value, end=" -> ")
#             current = current.next
#         print("None")
'''
 each element of the linked list is stored in a ListNode object,
 and the next attribute of each node points to the next node in
 the sequence. The entire linked list is essentially a chain of ListNode objects.
'''


# nums = [13, 24, 34, 44, 54]
# head = ListNode(nums[0])
# print ("head****", head.value)
# current = head
# print ('first current', current.value)
# for number in nums[1:]:
#     print ('current before current.next in the loop', current.value )
#     current.next = ListNode(number)
#     print ('current.next' , current.next.value)
#     print(ListNode(current) if ListNode else None)
#     current = current.next
#     print ('2nd current============>', current.value)
#     # print(ListNode(number) if ListNode else None)
# print ('current after exiting the loop', current.value)
# #nums = [13, 24, 34, 44, 54]

# current = head
# print ('current HEAD OOOOO---------------' , current.value)
# print (current.value)
# print (current.next.value if current.next else None)

# while current:
#     print (current.value)
#     print (current.next.value if current.next else None)
#     current = current.next
# # print (head)

# # Print the linked list as a nested dictionary
# linked_list_dict = head.to_dict()
# print(linked_list_dict)
# # Pretty-print the nested dictionary using json.dumps
# linked_list_json = json.dumps(linked_list_dict, indent=4)
# print(linked_list_json)

# head.print_linked_list()

#! 2- 206. Reverse Linked List (Algo Academy) (easy) (Tech: ? )  (time complexity: ?)
'''
206. Reverse Linked List
Easy
Topics
Companies Amazon Apple Bloomberg
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

'''
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None

#         def _helper(head, prev):
#         #    print('head', head.value if head else None)
#            if head is None:
#                return prev # if you return the hear or the prev is this case it returns the head and all relate linked list

#            next = head.next
#         #    print('next', next.value if next else None)
#            head.next = prev
#         #    print ('head.next',head.next.value if head.next else None)
#            return _helper(next,head)
#         return _helper(head,prev)

# # Convert the input list to a linked list
# head_values = [1, 2, 3, 4, 5]
# head = ListNode(head_values[0])
# current_node = head
# for value in head_values[1:]:
#     current_node.next = ListNode(value)
#     current_node = current_node.next

# # Create an instance of Solution
# solution = Solution()

# # Test the reverseList method
# reversed_head = solution.reverseList(head)

# # Print the reversed linked list values
# while reversed_head:
#     print(reversed_head.value, end=" ")
#     reversed_head = reversed_head.next

#! 3-just traverse through a node list

# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# class Solution:
#     def traverse(self, head: Optional[ListNode]) -> Optional[ListNode]:

#            if not head:
#                 return None
#            print (head.value)
#            return self.traverse(head.next)

#         #    current = head
#         #    while current:
#         #        current = current.next
#         #        print (current.value if current else None)
#         #    return None


# # Convert the input list to a linked list
# head_values = [1, 2, 3, 4, 5]
# head = ListNode(head_values[0])
# current_node = head
# for value in head_values[1:]:
#     current_node.next = ListNode(value)
#     current_node = current_node.next

# # Create an instance of Solution
# solution = Solution()
# reversed_head = solution.traverse(head)

#! 4- 876. Middle of the Linked List (algo: fast and alow pointers)

'''
876. Middle of the Linked List
Easy
Topics
Companies Adobe Oracle Google
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

'''

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

#          fast = slow = head
#          while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#          return slow



# head_values = [1, 2, 3, 4, 5, 6] #4
# head = ListNode(head_values[0])
# current_node = head
# for value in head_values[1:]:
#     current_node.next = ListNode(value)
#     current_node = current_node.next

# # Create an instance of Solution
# solution = Solution()
# print (solution.middleNode(head).val)


#! 5- 141. Linked List Cycle (algo: fast and alow pointers)

'''
141. Linked List Cycle
Easy
Topics
Companies
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if not head:
#             return False
#         fast = slow = head

#         while fast and fast.next :
#             fast = fast.next.next
#             slow = slow.next
#             if fast == slow:
#                 return True

#         return False




# # Example usage:
# # Construct the linked list
# head = ListNode(3)
# head.next = ListNode(2)
# head.next.next = ListNode(0)
# head.next.next.next = ListNode(-4)
# head.next.next.next.next = head.next  # Creating a cycle
# solution = Solution()
# print(solution.hasCycle(head))  # Output: True


#! 6- 21. Merge Two Sorted Lists

'''

21. Merge Two Sorted Lists
Easy
Topics
Companies Amazon Expedia Apple
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        if list2 == None: return list1

        if list1.val < list2.val:
            next1 = list1.next
            list1.next = self.mergeTwoLists(next1,list2)
            return list1
        else:
            next2 = list2.next
            list2.next = self.mergeTwoLists(list1,next2)
            return list2



# list1 = [1,2,4] # [1,1,2,3,4,4]
# list2 = [1,3,4]
# Create ListNode objects for list1 and list2
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
