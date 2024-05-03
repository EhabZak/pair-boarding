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
