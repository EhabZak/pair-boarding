import math
import os
import random
import re
import sys
import json

#! to create a node
class ListNode:
    def __init__(self, value=0, next= None):
        self.value = value
        self.next = next

nums = [13, 24, 34, 44, 54]
head = ListNode(nums[0])
current = head
for number in nums[1:]:
    current.next = ListNode(number)
    current = current.next
current = head
while current:
    print (current.value)
    print (current.next.value if current.next else None)
    current = current.next


#! to create a node with lots of prints
class ListNode:
    def __init__(self, value=0, next= None):
        self.value = value
        self.next = next
#! if you want to print the node as a string add this function
    def __str__(self):
        # Convert the ListNode instance to a string representation
        return f"ListNode(value={self.value}, next={self.next})"
#! if you want to print the node as a dictionary add this function
    def to_dict(self):
        if self.next is not None:
            return {'value': self.value, 'next': self.next.to_dict()}
        else:
            return {'value': self.value, 'next': None}
#! if you want to print the node as a linked list shape add this function
    def print_linked_list(self):
        current = self
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
'''
 each element of the linked list is stored in a ListNode object,
 and the next attribute of each node points to the next node in
 the sequence. The entire linked list is essentially a chain of ListNode objects.
'''


nums = [13, 24, 34, 44, 54]
head = ListNode(nums[0])
print ("head****", head.value)
current = head
print ('first current', current.value)
for number in nums[1:]:
    print ('current before current.next in the loop', current.value )
    current.next = ListNode(number)
    print ('current.next' , current.next.value)
    print(ListNode(current) if ListNode else None)
    current = current.next
    print ('2nd current============>', current.value)
    # print(ListNode(number) if ListNode else None)
print ('current after exiting the loop', current.value)
#nums = [13, 24, 34, 44, 54]

current = head
print ('current HEAD OOOOO---------------' , current.value)
print (current.value)
print (current.next.value if current.next else None)

while current:
    print (current.value)
    print (current.next.value if current.next else None)
    current = current.next
# print (head)

# Print the linked list as a nested dictionary
linked_list_dict = head.to_dict()
print(linked_list_dict)
# Pretty-print the nested dictionary using json.dumps
linked_list_json = json.dumps(linked_list_dict, indent=4)
print(linked_list_json)

head.print_linked_list()
