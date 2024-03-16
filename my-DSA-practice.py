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
        return True



    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        lastElement, idx = self.list[-1], self.map[val]
        self.list[idx], self.map[lastElement] = lastElement, idx
        self.list.pop()
        del self.map[val]
        return True






    def getRandom(self) -> int:
        return random.choice(self.list)





randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))  # Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomizedSet.remove(2))  # Returns false as 2 does not exist in the set.
print(randomizedSet.insert(2))  # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.insert(3))  # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom())  # getRandom() should return either 1 or 2 randomly.
print(randomizedSet.remove(1))  # Removes 1 from the set, returns true. Set now contains [2].
print(randomizedSet.insert(2))  # 2 was already in the set, so return false.
print(randomizedSet.getRandom())
