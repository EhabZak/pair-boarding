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
                current.children[char] = Node()
            current = current.children[char]
        current.endOfWord = True

###########################################################
    def search(self, word: str) -> bool:
        def dfs(index,root):
            current = root

            for i in range(index,len(word)):
                char = word[i]
                if char == '.':
                    for child in current.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False
                    current = current.children[char]
            return current.endOfWord

        return dfs(0,self.root)



##############################################################




class Node:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

    def __repr__(self):
        return f"Node(children={self.children}, endOfWord={self.endOfWord})"




'''

do this in python
let num = [0, 1, 0, 3, 12]

function check(numbers) {

    for (let i in numbers) {

        number = numbers[i]
        if (number == 0) {

            let num1 = numbers.splice(i, 1)
            console.log(num1)
            numbers.push(number)
        }

    }

    console.log(numbers)

}

check(num)

'''
