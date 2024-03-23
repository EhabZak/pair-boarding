from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll =DoubleLinkedList() # creates only one double linked list # there is only one instance of double linked list
        self.hash = {}
