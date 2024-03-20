from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DoubleLinkedList()
        self.hash = {}


    def get(self, key: int) -> int:
        pass





    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.dll.remove(self.hash[key])
        newNode = Node(key,value)
        self.hash[key]= self.dll.push(newNode)
        if self.dll.length > self.capacity:
            lru = self.dll.head.next # why is lru a dictionary ?
            del self.hash[lru.key]




class Node:
    def __init__(self,val,key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, node) -> None:
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

        def remove(self, node):
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
            self.length -=1

        def push (self, node):
            prev = self.tail.prev
            nxt = self.tail
            prev.next = node
            nxt.prev = node

            node.next = nxt
            node.prev = prev

            self.length +=1
            return node











    # add


    #remove












    def print_list(self):
        current =self.head
        values = []
        while current != self.tail:
            if current.key is not None and current.val is not None:
                values.append(f"({current.key}, {current.val})")
            current = current.next
        print ("double linked list:"+"<->".join(values))






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

    # Instantiate the LRUCache object with capacity 2
cache = LRUCache(2)

# Perform operations as specified in the input
print(cache.put(1, 1))  # Put key=1, value=1
print(cache.put(2, 2))  # Put key=2, value=2
print(cache.get(1))     # Get value associated with key=1 (Expected output: 1)
print(cache.put(3, 3))  # Put key=3, value=3
print(cache.get(2))     # Get value associated with key=2 (Expected output: -1, as key 2 was evicted by key 3)
print(cache.put(4, 4))  # Put key=4, value=4
print(cache.get(1))     # Get value associated with key=1 (Expected output: -1, as key 1 was evicted by key 4)
print(cache.get(3))     # Get value associated with key=3 (Expected output: 3)
print(cache.get(4))     # Get value associated with key=4 (Expected output: 4)
