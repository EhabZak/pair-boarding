from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list= []



    def insert(self, val: int) -> bool:
        self.map = {}
        self.list = []
        if val in self.map:
            return False
        self.list.append(val)
        self.map[val] = len(self.list)-1



    def remove(self, val: int) -> bool:






    def getRandom(self) -> int:





randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))  # Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomizedSet.remove(2))  # Returns false as 2 does not exist in the set.
print(randomizedSet.insert(2))  # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.insert(3))  # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom())  # getRandom() should return either 1 or 2 randomly.
print(randomizedSet.remove(1))  # Removes 1 from the set, returns true. Set now contains [2].
print(randomizedSet.insert(2))  # 2 was already in the set, so return false.
print(randomizedSet.getRandom())
