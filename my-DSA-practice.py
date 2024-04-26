from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random

class WordDictionary:

    def __init__(self):
        self.root = Node()


    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char]= Node()

            current = current.children[char]
        current.endOfWord = True


    def search(self, word: str) -> bool:
        current = self.root

        def dfs(index,root):
            current = root #! ????

            for i in range(index,len(word)):
                char = word[i]
                if char == '.':
                    for child in current.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False
                    current = current.children[char]
            return current.endOfWord
        return dfs(0,self.root)





class Node:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False
    def __repr__(self):
        return f"Node(children={self.children}, endOfWord={self.endOfWord})"


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Test the WordDictionary class
if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))  # Expected output: False
    print(wordDictionary.search("bad"))  # Expected output: True
    print(wordDictionary.search(".ad"))  # Expected output: True
    print(wordDictionary.search("b.."))  # Expected output: True
