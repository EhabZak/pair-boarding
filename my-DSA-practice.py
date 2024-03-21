from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class LRUCache:

    def __init__(self, capacity: int):
        pass




    def get(self, key: int) -> int:
        pass






    def put(self, key: int, value: int) -> None:
        pass


















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
