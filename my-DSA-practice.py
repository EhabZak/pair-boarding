from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Trie:

    def __init__(self):
        self.root = Node()



    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            i = ord(char) - ord('a')
            if current.children[i] ==None:
                current.children[i] == Node()
            current = current.children[i]
        current.endOfWord = True
    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            i = ord(char)- ord('a')
            if current.children[i]==None:
                return False
        return current.endOfWord





    def startsWith(self, prefix: str) -> bool:
        pass



class Node:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False



def test_trie():
    trie = Trie()
    actions = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    values = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    expected_output = [None, None, True, False, True, None, True]

    for action, value, expected in zip(actions, values, expected_output):
        if action == "Trie":
            trie = Trie()
            print("Trie initialized.")
        elif action == "insert":
            trie.insert(*value)
            print(f"Inserted '{value[0]}' into Trie.")
        elif action == "search":
            result = trie.search(*value)
            print(f"Search for '{value[0]}': {result}. Expected: {expected}")
        elif action == "startsWith":
            result = trie.startsWith(*value)
            print(f"StartsWith '{value[0]}': {result}. Expected: {expected}")

test_trie()
