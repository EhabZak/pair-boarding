from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random

class WordDictionary:

    def __init__(self):
        current = self.root


    def addWord(self, word: str) -> None:

###########################################################
    def search(self, word: str) -> bool:
        pass



##############################################################




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
    # wordDictionary.addWord("dad")
    # wordDictionary.addWord("mad")
    # print(wordDictionary.search("pad"))  # Expected output: False
    # print(wordDictionary.search("bad"))  # Expected output: True
    print(wordDictionary.search(".ad"))  # Expected output: True
    # print(wordDictionary.search("b.."))  # Expected output: True


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
