from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import json
import heapq
import math
import random

#! 1- DFS problem
'''   0
    /  |  \
   1   2   3
/   \  /
4     5
  '''
# ad_max = [
#   # these columns represent the relationship
#    #0 1 2 3 4 5          # print ad-max[n]
#    [0,1,1,1,0,0],#0    # 0 line 2 times  # 5 line 5 times # this line represents the node 0
#    [1,0,0,0,1,1],#1    # 1 line 5 times  # 3 line 6 times
#    [1,0,0,0,0,1],#2    # 4 line 6 time   # 0 line 2 times
#    [1,0,0,0,0,0],#3    # 2 line 1  time
#    [0,1,0,0,0,0],#4    # 5 line 3  time
#    [0,1,1,0,0,0] #5    # 2 line 6  time
# ]
# visited= [0,0,0,0,0,0] #indicates if a node has been visited or not
# # n = means a node
# #what are the numbers in the matrix? relationships to the node
# #what are the numbers in visited? tracking the status of the node if visited or not
# #where is the relation? in the matrix columns the rows represent the nodes
# # why is relation different when we put it in the for loop and outside the for loop?
# #where is the visited?
# #where is the n? n = node the rows are the nodes or the n
# # what is num? why do we have it? it represent the index of the numbers (which represent the relationship) in the ad_max[n] so the arrays in the ad_max array
# def dfs (n):
#     if visited[n] != 0: #! this is the base case
#         return
#     else:
#         visited[n] = 1 # this means if node is not visited then mark it as visited
#         num = 0 #! num is initiated here it means start at index zero in the ad_max[n]
#         for relation in ad_max[n]: # for the numbers in the array of node 0 = [0,1,1,1,0,0]

#             if relation != 0:
#                 dfs(num) # recursively calls the dfs function for each adjacent node that is connected.
#             num = num + 1 # this will be used to iterate over the adjacent nodes of the current node n

#         print (n)


# # src_node = int(input('Enter the source node: '))
# src_node = int(0)
# dfs(src_node)
# print (dfs(0)) # if you select 0 as source node the output will be 4 2 5 1 3 0 this shows how the nodes are traversed and popped off the stack

# you can also do it like in mode 6 for both dfs and bfs and then solve the problems
# don't forget that there are also sort methods

#! 2-problem 22 leet code - Generate Parentheses
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         close_to_open = {
#             ')': '(',
#             ']': '[',
#             '}': '{'
#             }
#         for char in s:
#             # if char in close_to_open:
#             #     print(char)
#             if char not in close_to_open:
#                 # print(char)
#                 stack.append(char)
#             elif not stack or stack[-1] != close_to_open[char]:
#                 return False
#             else:
#                 stack.pop()
#         return len(stack) == 0

# # Create an instance of the Solution class
# solution_instance = Solution()

# # Call the isValid method with the given string
# result = solution_instance.isValid("()[]{}")

# # Print the result
# print(result)

#! 3-problem 1535 leet code (alex weekly lecture) - Find the Winner of an Array Game
'''
1535. Find the Winner of an Array Game
#!Medium

Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]).
In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains
at position 0, and the smaller integer moves to the end of the array. The game ends when an integer
wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.


Example 1:

Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
Example 2:

Input: arr = [3,2,1], k = 10
Output: 3
Explanation: 3 will win the first 10 rounds consecutively.


Constraints:

2 <= arr.length <= 105
1 <= arr[i] <= 106
arr contains distinct integers.
1 <= k <= 109


'''
# from collections import deque
# from typing import List # it should be already there if ver is 3.7 and higher I also installed it using pip install typing but still not defined
# class Solution:
#     def getWinner(self, arr: List[int], k: int) -> int:
#     # def getWinner(self, arr, k):
#         if k>= len(arr):
#             return max(arr)
#         wins = 0
#         curr_winner = arr[0]
#         queue = deque(arr[1::])
#         # print('queue =====>>>', queue)
#         while wins < k :
#             opponent = queue.popleft()
#             print('queue =====>>>', queue)
#             if curr_winner > opponent:
#                 queue.append(opponent)
#                 wins += 1
#             else:
#                 queue.append(curr_winner)
#                 curr_winner = opponent
#                 wins = 1
#         return curr_winner

# arr = [2, 1, 3, 5, 4, 6, 7]
# k = 2
# # arr = [3,2,1]
# # k = 10

# solution_instance = Solution()
# result = solution_instance.getWinner(arr, k)
# print(result)


#! 4-problem 501 leet code (alex weekly lecture) -Find Mode in Binary Search Tree (Tech: DFS)

'''
501. Find Mode in Binary Search Tree
#!Easy

Given the root of a binary search tree (BST) with duplicates, return all the mode(s)
(i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
'''

# from typing import Optional, List
# from collections import defaultdict
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def findMode(self, root: Optional[TreeNode]) -> List[int]:
#         frequencies = defaultdict(int)
#         # print ("frequencies ===", frequencies) # don't put it here it will not give you the correct dictionary
#         def _dfs(node):
#             # base case
#             if not node:
#                 return
#             # do the thing (what ever you are required to do for the problem)
#             # so here we increase the count in the dictionary
#             frequencies[node.val] += 1
#             _dfs(node.left)
#             _dfs(node.right)   # this is a boiler plate for DFS (a helper function to traverse the tree)

#         _dfs(root)  # the root does not change only the node changes in the traversing
#         # print ("frequencies ===>", frequencies)
#         # print ("frequencies ===>", dict(frequencies))
#         max_freq = max(frequencies.values())
#         res = []

#         for node in frequencies:
#             if frequencies[node] == max_freq:
#                 res.append(node)
#         return res
# '''
#     1
#      \
#       2
#      /
#     2
# '''

# root = TreeNode(1, None, TreeNode(2, TreeNode(2), None))

# # Create a bigger binary tree
# # root = TreeNode(5,
#                 # left=TreeNode(3, TreeNode(1), TreeNode(5)),
#                 # right=TreeNode(8, TreeNode(7), TreeNode(9)))
# '''
#         5
#        / \
#       3   8
#      /|   |\
#     1 5   7 9

# '''
# # Create an instance of the Solution class
# solution = Solution()

# # Call the findMode method and print the result
# output = solution.findMode(root)
# print(output)

#! 5-problem 56 leet code (App Academy course) - Merge Intervals

'''
56. Merge Intervals
Medium
21.2K
727
Companies
Given an array of intervals where intervals[i] = [starti, endi],
 merge all overlapping intervals, and return an array of the
 non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

'''
# from typing import List
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         print (intervals)
#         intervals.sort()
#         print (intervals)
#         stack = [intervals[0]]

#         for i in range(1, len(intervals)):
#             curr_int ={
#                 'start': intervals[i][0],
#                 'end': intervals[i][1]
#             }
#             last_int_index = len(stack)-1

#             last_int ={
#                 'start': stack[last_int_index][0],
#                 'end': stack[last_int_index][1]
#             }

#             if curr_int['start'] <= last_int['end'] and curr_int['end'] > last_int['end']:
#                 stack[last_int_index][1] = curr_int['end']
#             elif curr_int['start'] > last_int['end']:
#                 stack.append(intervals[i])

#         return stack

# # intervals = [[1,3],[2,6],[8,10],[15,18]]
# # intervals = [[1,3],[2,6],[11,16],[15,18]] # output [[1, 6], [11, 18]
# # intervals = [[1,3],[2,6],[11,16],[10,18]] # output [[1, 6], [10, 18]] this one does not work correctly
# intervals = [[1,3],[11,16],[10,18],[2,6]] # output [[1, 6], [10, 18]]

# solution = Solution()
# output = solution.merge(intervals)
# print(output)

#! 6- problem 1. Two Sum

'''
companies Amazon Apple Adobe
Given an array of integers nums and an integer target, return indices of the two numbers such that they
add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

'''
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#                     """
#         hash={}

#         for i, num in enumerate(nums): # [(0, 2), (1, 7), (2, 11), (3, 15)]
#             complement = target - num
#             if complement in hash:
#                 return [i,hash[complement]]
#             hash[num] = i

#! mock interview solution

 # create a hash
        # we iterate through the list
        # if number - target exists in hash we return the indices
        #  s= {}

        #  for i in range(len(nums)):
        #      number = nums[i]
        #      complement =  target - number
        #      if complement in s:
        #          return [s[complement], i]
        #      else:
        #          s[number] = i

# nums = [2,7,11,15] #  [1, 0]
# target = 9
# solution = Solution()
# output = solution.twoSum(nums, target)
# print(output)


# numss = [2,7,11,15]
# numbers = list(enumerate(numss))
# # print (List(numbers))
# print (numbers)




#! 7-  2482. Difference Between Ones and Zeros in Row and Column
'''
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.



Example 1:

Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]

Example 2:
Input: grid = [[1,1,1],[1,1,1]]
Output: [[5,5,5],[5,5,5]]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
grid[i][j] is either 0 or 1.
'''

#keep track of number of zeros and ones for each row and col
# can use arrays to keep track of these since they're 0-index


# class Solution(object):
#     def onesMinusZeros(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: List[List[int]]
#         """

#         ROWS = len (grid)
#         COLS = len(grid[0])

#         difference =[[0 for _ in range (COLS)] for _ in range (ROWS)] # this is to create a 2D array
#         print( 'difference' ,difference)

#         row_ones = [0]*ROWS
#         col_ones = [0]*COLS

#         for r in range (ROWS):
#            for c in range (COLS):
#             if grid[r][c] == 1:
#               row_ones[r] += 1
#               col_ones [c] += 1
#         print (row_ones, col_ones)

#         for r in range (ROWS):
#            for c in range (COLS):
#               difference[r][c] = row_ones[r] + col_ones [c] - (ROWS - row_ones[r]) - (COLS- col_ones[c])

#         return difference

# grid = [[0,1,1],[1,0,1],[0,0,1],[1,0,1]]
# solution = Solution()
# output = solution.onesMinusZeros(grid)
# print(output)

#! 8- Problem 73. Set Matrix Zeroes (Algo Academy)(medium) (Tech: Hash map)
'''
companies: Microsoft Bloomberg Amazon
Given an m x n integer matrix matrix, if an element is 0,
 set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

'''
# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         rows = set()
#         cols = set()
#         print (rows)

#         for r in range(len(matrix)):
#            for c in range(len(matrix[0])):
#               if matrix[r][c] == 0:
#                  rows.add(r)
#                  cols.add(c)
#         for r in range(len(matrix)):
#            for c in range(len(matrix[0])):
#               if r in rows or c in cols :
#                  matrix [r][c] = 0
#         print (rows)

# matrix = [[1,1,1],[1,0,1],[1,1,1]] # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
# # matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] #  [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
# solution = Solution()
# solution.setZeroes(matrix)
# print(matrix)

'''
The setZeroes method in your Solution class doesn't have a return statement, and it modifies
 the matrix in-place. Therefore, when you call solution.setZeroes(matrix), it doesn't return
   anything (None is implicitly returned since there's no explicit return statement),
   and the value of output2 becomes None
'''

#! 9-1160. Find Words That Can Be Formed by Characters -(Lecture) -(Easy)

'''
1160. Find Words That Can Be Formed by Characters
#! Easy

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.




'''
# class Solution(object):
#     def countCharacters(self, words, chars):
#         """
#         :type words: List[str]
#         :type chars: str
#         :rtype: int
#         """
#         total = 0
#         count = Counter(chars)
#       #   print(count)

#         for word in words:
#             word_count = Counter(word)
#             # print(word_count)

#             valid = True

#             for key in word_count:

#                #  print( key , ":" , word_count[key])

#                 if key not in count or count[key] < word_count[key]:
#                     valid = False
#                     break
#             if valid:
#                 total += len(word)
#         return total




# # words = ["cat","bt","hat","tree"]
# # chars = "atach"
# words = ["hello","world","leetcode"]
# chars = "welldonehoneyr"

# solution = Solution()
# output = solution.countCharacters(words, chars)
# print(output)

#! 10- 682. Baseball Game (Algo-Academy)-(Easy)

'''

Easy

Companies UBER, Amazon
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.



Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

'''
# class Solution(object):
#     def calPoints(self, operations):
#         """
#         :type operations: List[str]
#         :rtype: int
#         """
#         stack = []

#         for op in operations:
#             if op == '+':
#                 stack.append(stack[-1]+stack[-2])
#             elif op == 'C':
#                 stack.pop()
#             elif op =='D':
#                 stack.append(2*stack[-1])
#             else:
#                 stack.append(int(op))

#         return sum(stack)

# # ops = ["5","2","C","D","+"] #30
# ops = ["5","-2","4","C","D","9","+","+"] #27
# solution = Solution()
# output = solution.calPoints(ops)
# print(output)

#! 11- 217. Contains Duplicate-(Lecture)-(Easy)

'''
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

'''


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
        #! good time but bad space complexity
        # setArray = set()
        # for i in nums:
        # # checks if the element is already present in the set, if yes returns true
        #     if i in setArray:
        #         return True
        # # if the element is not present then it gets added into the set
        #     else:
        #         setArray.add(i)

        # return False
    #! bad time but good space complexity
        # nums.sort()
        # for index in range(len(nums)-1):
        #       if nums[index] == nums[index + 1]:
        #            return True
        # return False

#! bad time but good space complexity
#      num_counts = Counter(nums)

#      for count in num_counts.values():
#         if count > 1:
#             return True

#      return False

# # nums = [1,1,1,3,3,4,3,2,4,2] # True
# # nums = [1,2,3,4] # False
# solution = Solution()
# output = solution.containsDuplicate(nums)
# print(output)

#! 12- 219. Contains Duplicate II (Algo Academy) (Easy) (Tech: static sliding window)

'''
219. Contains Duplicate II
Easy

Companies ( Amazon, Facebook, Adobe)
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.

'''

# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         window = set()
#         left = 0

#         for right in range(len(nums)):
#             print('window', window)
#             print('right', nums[right])
#             print('left' , nums[left])
#             if right-left > k:
#                 window.discard(nums[left])
#                 left += 1

#             if nums[right] in window:
#                 return True

#             window.add(nums[right])


#         return False

# nums = [1,2,3,1] # True
# k = 3

# # nums = [11,0,11,11] # True
# # k = 1

# # nums = [1,2,3,1,2,3] # False
# # k = 2

# solution = Solution()
# output = solution.containsNearbyDuplicate(nums, k)
# print(output)

#! 13- 3. Longest Substring Without Repeating Characters (Algo Academy) (medium) (Tech: variable sliding window)
'''
3. Longest Substring Without Repeating Characters
Medium
38.4K
1.8K
Companies
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''



# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         left, right = 0 , 0
#         max_length = 0
#         window = set()

#         while right < len(s):
#             # print('window', window)
#             # print('left' , s[left])
#             # print('right', s[right])
#             while s[right] in window:
#                 window.discard(s[left])
#                 left += 1

#             max_length = max(max_length, right-left+1)
#             window.add(s[right])
#             right +=1

#         return max_length
# '''
# in this question we used a while loop in the 2nd loop and not if
#  because The while loop continues to execute as long as the condition s[right] in window is true
#  The if statement is executed only once per outer loop iteration.
# '''

# s = "abcabcbb"
# solution = Solution()
# output = solution.lengthOfLongestSubstring(s)
# print(output)

#! 14- 167. Two Sum II - Input Array Is Sorted (Algo Academy) (medium) (Tech: two points)

'''
167. Two Sum II - Input Array Is Sorted
Medium
Topics
Companies Bloomberg Adobe Amazon
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

'''

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left, right = 0, len(numbers)-1

#         while left< right:
#             sum = numbers[left]+ numbers[right]
#             print ("L", left)
#             print ("R", right)
#             print ('sum' , sum)


#             if sum > target:
#                 right -= 1
#             elif sum < target:
#                 left += 1
#             else:
#                 return [left+1, right+1]

# # numbers = [2,7,11,15] # [1,2]
# # target = 9
# # numbers = [2,3,4] # [1,3]
# # target = 6
# numbers = [5,25,75] # [2,3]
# target = 100
# solution = Solution()
# output = solution.twoSum(numbers, target)
# print(output)


#! 15- 11. Container With Most Water (Algo Academy) (medium) (Tech: two points)

'''
11. Container With Most Water
Medium
Topics
Companies Apple, Adobe, Amazon
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

'''
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_water,left,right = 0, 0, len(height)-1

#         while left < right:
#             shorter = min(height[right], height[left])

#             area = (right-left) * shorter

#             max_water = max(max_water, area)


#             if height[left] >= height[right]:
#                 right -= 1
#             else:
#                 left += 1

#         return max_water

# height = [1,8,6,2,5,4,8,3,7]
# solution = Solution()
# output = solution.maxArea(height)
# print(output)

#! 16- 209. Minimum Size Sub-array Sum (Algo Academy) (medium) (Tech: variable sliding window)

'''

Medium

Companies Microsoft Amazon google
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another
solution of which the time complexity is O(n log(n)).

'''

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         left,total, min_sub = 0,0, float('inf')

#         for right in range (len(nums)):
#             total += nums[right]

#             while total >= target:
#                 min_sub = min(min_sub, right-left+1 )
#                 total -= nums[left]
#                 left += 1
#         return 0 if min_sub == float('inf') else min_sub


# target = 7
# nums = [2,3,1,2,4,3]
# solution = Solution()
# output = solution.minSubArrayLen(target, nums)
# print(output)

#! 17-49. Group Anagrams (Algo Academy) (medium) (Tech: Hash map)
#(time complexity: O(n.s logs)) n is s in the loop and s is the sorted(s)
# space complexity is On

'''
49. Group Anagrams
Medium
Topics
Companies Amazon Adobe Yandex
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

'''

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups = defaultdict(list)

#         for s in strs:
#             key = "".join(sorted(s))
#             # print("s===>", s)
#             # print ("KEY+++>",key)
#             # print("groups", groups)
#             groups[key].append(s)

#         return groups.values()


# strs = ["eat","tea","tan","ate","nat","bat"]
# solution = Solution()
# output = solution.groupAnagrams(strs)
# print(output)

#! 18-36. Valid Sudoku (Algo Academy) (medium) (Tech: defaultdict and set)

'''
36. Valid Sudoku
Medium
Topics
Companies Amazon Apple Karat
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.


'''
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:

#         row = defaultdict(set)
#         col = defaultdict(set)
#         box = defaultdict(set)

#         for r in range(len(board)):
#             for c in range(len(board[0])):
#                 curr_val = board[r][c]

#                 if curr_val != '.':
#                     box_coord =f'{r//3}, {c//3}'

#                     if curr_val in row[r] or curr_val in col[c] or curr_val in box[box_coord]:
#                         return False

#                     row[r].add(curr_val)
#                     col[c].add(curr_val)
#                     box[box_coord].add(curr_val)
#                     # print('box===>', box)
#         return True


# # board = [["5","3",".",".","7",".",".",".","."]
# #         ,["6",".",".","1","9","5",".",".","."]
# #         ,[".","9","8",".",".",".",".","6","."]
# #         ,["8",".",".",".","6",".",".",".","3"]
# #         ,["4",".",".","8",".","3",".",".","1"]
# #         ,["7",".",".",".","2",".",".",".","6"]
# #         ,[".","6",".",".",".",".","2","8","."]
# #         ,[".",".",".","4","1","9",".",".","5"]
# #         ,[".",".",".",".","8",".",".","7","9"]]
# # board = [["8","3",".",".","7",".",".",".","."]
# #         ,["6",".",".","1","9","5",".",".","."]
# #         ,[".","9","8",".",".",".",".","6","."]
# #         ,["8",".",".",".","6",".",".",".","3"]
# #         ,["4",".",".","8",".","3",".",".","1"]
# #         ,["7",".",".",".","2",".",".",".","6"]
# #         ,[".","6",".",".",".",".","2","8","."]
# #         ,[".",".",".","4","1","9",".",".","5"]
# #         ,[".",".",".",".","8",".",".","7","9"]]
# board = [[".","8","7","6","5","4","3","2","1"]
#          ,["2",".",".",".",".",".",".",".","."]
#          ,["3",".",".",".",".",".",".",".","."]
#          ,["4",".",".",".",".",".",".",".","."]
#          ,["5",".",".",".",".",".",".",".","."]
#          ,["6",".",".",".",".",".",".",".","."]
#          ,["7",".",".",".",".",".",".",".","."]
#          ,["8",".",".",".",".",".",".",".","."]
#          ,["9",".",".",".",".",".",".",".","."]]

# solution = Solution()
# output = solution.isValidSudoku(board)
# print(output)

#! 19-128. Longest Consecutive Sequence (Algo Academy) (medium) (Tech: ? )
'''
128. Longest Consecutive Sequence
Medium
Topics
Companies Amazon google Apple
Given an unsorted array of integers nums, return the length of
the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

'''
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         num_set = set(nums)
#         # print(num_set) # {1, 2, 3, 100, 4, 200}
#         longest = 0

#         for n in num_set:
#             # print ('n', n)
#             if (n-1) not in num_set:
#                 length = 0
#                 while (n+length) in num_set:
#                 # print('n+length===>', n+length)
#                     length += 1
#                 # print("length is++++++++++++++++++++ ", length)
#                 longest = max(length, longest)

#         return longest


# nums = [100,4,200,1,3,2]
# # nums = [100,101,102,103,1,3,2]
# nums = [0,-1]
# solution = Solution()
# output = solution.longestConsecutive(nums)
# print(output)




#! 19-74. Search a 2D Matrix (Algo Academy) (medium) (Tech: binary search )  (time complexityO(log(m * n)))

'''
74. Search a 2D Matrix
Medium
Topics
Companies Amazon Adobe Apple
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

'''
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         rows = len(matrix)
#         cols = len(matrix[0])

#         top,bottom = 0 , rows-1

#         while top <= bottom:
#             row = top + (bottom- top)//2

#             if target > matrix[row][cols-1]:
#                 top = row+1
#             elif target < matrix[row][0]:
#                 bottom = row -1
#             else:
#                 break

#         if top > bottom:
#             return False

#         row = top + (bottom - top)//2
#         left, right = 0 , cols-1
#         while left <= right:
#             mid = left + (right-left)//2
#             if target > matrix[row][mid]: # it is a value not an index that why you don't just use mid
#                 left = mid+1
#             elif target < matrix[row][mid]:
#                 right = mid -1
#             else:
#                 return True
#         return False



# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
# solution = Solution()
# output = solution.searchMatrix(matrix,target)
# print(output)


#! 20-162. Find Peak Element (Algo Academy) (medium) (Tech: binary search )  (time complexityO(log (n)))

'''
162. Find Peak Element
Medium
Topics
Companies
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

# '''
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         #! iterative approach
#         left, right = 0 , len(nums)-1
#         while left < right:
#             mid = left +(right-left)//2 # this is left + ((right-left)//2)
#             print ('mid', mid)
#             if nums[mid] < nums [mid+1]:
#                 left = mid+1
#                 print('left is ++++>', left)
#             else:
#                 right = mid
#                 print('right is ===>', right)
#         return left # it is like saying when left = right
#         #! recursive approach
#         def _search(left,right):
#             if left == right: return left

#             mid = left + (right-left)//2

#             if nums[mid]< nums[mid+1]:
#                 return _search(mid+1, right)
#             else:
#                 return _search(left,mid)

#         return _search(0,len(nums)-1)

# # nums = [1,2,3,1] #2
# nums = [1,2,1,3,5,6,4] #5

# solution = Solution()
# output = solution.findPeakElement(nums)
# print(output)


#! this is

#! 21- 509. Fibonacci Number (Algo Academy) (medium) (Tech: recursion)  (time complexityO(2**n))


'''
509. Fibonacci Number
Easy
Topics
Companies
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).



Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Constraints:

0 <= n <= 30

'''

# class Solution:
#     def fib(self, n: int) -> int:

#         if n == 0 : return 0
#         if n == 1 : return 1

#         return self.fib(n-1)+ self.fib(n-2)


# n = 10
# solution = Solution()
# output = solution.fib(n)
# print(output)



#!22- 575. Distribute Candies  (easy) (Tech: just a set) (Mock interview)


'''
575. Distribute Candies
Easy
Topics
Companies
Hint
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.



Example 1:

Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
Example 2:

Input: candyType = [1,1,2,3]
Output: 2
Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.
Example 3:

Input: candyType = [6,6,6,6]
Output: 1
Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.


Constraints:

n == candyType.length
2 <= n <= 104
n is even.
-105 <= candyType[i] <= 105

'''

# class Solution:
#     def distributeCandies(self, candyType: List[int]) -> int:

#         s = set(candyType)
#         ls = len(s)
#         length = len(candyType)//2

#         return min (ls, length)


# candyType = [1,1,2,2,3,3]

# solution = Solution()
# output = solution.distributeCandies(candyType)
# print(output)


#! 23 - 62. Unique Paths (Algo Academy) (medium) (Tech: ??)  (time complexity O(2^(m+n)) very bad)
'''
62. Unique Paths
Medium
Topics
Companies
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:

1 <= m, n <= 100

'''

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def path_count(m,n):
#             if m == 0 or n == 0 :  # if  0 means no further moves are possible
#                 return 0
#             elif m == 1 and n == 1: # if both aer 1 it means it reached the destination
#                 return 1
#             return path_count(m-1, n) + path_count(m, n-1)
#         return path_count(m,n)
# '''
# it starts finding the paths from the bottom because of the recursion and goes to  0,0 to find the paths
# it can be 0,0 and target be m-1 , n-1 or it can be 1,1 and m and n when you draw the grid.
# this solution didn't pass on leet code because it is too slow there is another dynamic programming solution that is better.
# '''
# m = 3
# n = 2

# solution = Solution()
# output = solution.uniquePaths(m,n)
# print(output)

#! 24-700. Search in a Binary Search Tree (Algo Academy) (easy) (algo: binary search)  (time complexityO(??))
'''
700. Search in a Binary Search Tree
Easy
Topics
Companies Adobe Amazon Microsoft
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return
 the subtree rooted with that node. If such a node does not exist, return null.



Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root: return None

#         if val< root.val:
#             return self.searchBST(root.left, val)
#         elif val > root.val:
#             return self.searchBST(root.right, val)
#         else:
#             return root


# root = [4,2,7,1,3]
# # Create the binary search tree
# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)

# # Example 1
# val1 = 2
# solution= Solution()
# result = solution.searchBST(root, val1)
# if result is not None:
#     print(result.val)
# else:
#     print("Node with value {} not found".format(val1))

#! 25-94. Binary Tree Inorder Traversal (Algo Academy) (easy) (algo: dfs)  (time complexity O(n))

'''
94. Binary Tree Inorder Traversal
Easy
Topics
Companies
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None: return []

#         left = self.inorderTraversal(root.left)
#         right = self.inorderTraversal(root.right)
#         return left + [root.val] + right  #[[], 1, [ [ [], 3, [] ], 2, [] ]]

# # root = [1,null,2,3]

# # Create a binary tree
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)

# # Instantiate the Solution class
# sol = Solution()

# # Test the inorderTraversal method
# result = sol.inorderTraversal(root)
# print(result)  # Output should be [1, 3, 2]

#! 25-144. Binary Tree Preorder Traversal (Algo Academy) (easy) (algo: dfs)  (time complexity O(n))

'''
144. Binary Tree Preorder Traversal
Easy
Topics
Companies Google Apple Microsoft
Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None: return []

#         left = self.preorderTraversal(root.left)
#         right = self.preorderTraversal(root.right)
#         return  [root.val]+ left + right



# # Create a binary tree
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)

# # Instantiate the Solution class
# sol = Solution()

# # Test the inorderTraversal method
# result = sol.preorderTraversal(root)
# print(result)  # Output should be [1, 3, 2]

#! 26-145. Binary Tree Postorder Traversal (Algo Academy) (easy) (algo: dfs)  (time complexity O(n))

'''
145. Binary Tree Postorder Traversal
Easy
Topics
Companies Bloomberg facebook Apple
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None: return []

#         left = self.postorderTraversal(root.left)
#         right = self.postorderTraversal(root.right)
#         return   left + right +[root.val]


# # Create a binary tree
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)

# # Instantiate the Solution class
# sol = Solution()

# # Test the inorderTraversal method
# result = sol.postorderTraversal(root)
# print(result)  # Output should be [3, 2, 1]


#! 27-  102. Binary Tree Level Order Traversal (Algo Academy) (Medium) (algo: bfs)  (time complexity O(n))

'''
102. Binary Tree Level Order Traversal
Medium
Topics
Companies Bloomberg Amazom Linkedin
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
    3
   / \
  9   20
     / \
    15  7
'''

## Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#           #! boiler plate for BFS
#         # queue = deque()
#         # queue.append(root)
#         # output = []
#         # while queue:
#         #     # shift out of the queue
#         #     node = queue.popleft()
#         #     if node:
#         #         output.append(node.val)
#         #         #adding children to the queue
#         #         queue.append(node.left)
#         #         queue.append(node.right)
#         # return output
#           #! solution
#           queue = deque()
#           queue.append(root)
#           output = []

#           while queue:
#             queueLen= len(queue)
#             print (' this is the queue ************', queue)
#             print('queuelen', queueLen)
#             level = []
#             for i in range(queueLen):
#                 print ('i ==>',i)

#                 node = queue.popleft()
#                 if node:
#                     level.append(node.val)
#                     queue.append(node.left)
#                     queue.append(node.right)
#             if level:
#                 output.append(level)

#           return output


# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# solution = Solution()
# print(solution.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]


#! 28- 100. Same Tree (Algo Academy) (easy) (algo: dfs)  (time complexity O(n))

'''
100. Same Tree
Easy
Topics
Companies Amazon linkedIn google
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

'''
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

#         if not p and not q: return True
#         if not p or not q: return False
#         if p.val != q.val: return False
#         print (p.val if p.val else None, q.val if q.val else None)


#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# ## example 1
# # p1 = TreeNode(1)
# # p1.left = TreeNode(2)
# # p1.right = TreeNode(3)

# # q1 = TreeNode(1)
# # q1.left = TreeNode(2)
# # q1.right = TreeNode(3)



#     # Example 3
# p1 = TreeNode(1)
# p1.left = TreeNode(2)
# p1.right = TreeNode(1)

# q1 = TreeNode(1)
# q1.left = TreeNode(1)
# q1.right = TreeNode(2)

# solution = Solution()
# print (solution.isSameTree(p1, q1))

#! 29- 104. Maximum Depth of Binary Tree (Algo Academy) (easy) (algo: dfs)  (time complexity O(n))

'''
104. Maximum Depth of Binary Tree
Easy
Topics
Companies Apple Amazon Google
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

'''
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root: return 0
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)
#         return max(left,right) + 1



# root1 = TreeNode(3)
# root1.left = TreeNode(9)
# root1.right = TreeNode(20)
# root1.right.left = TreeNode(15)
# root1.right.right = TreeNode(7)

# solution = Solution()
# print (solution.maxDepth(root1))

#! 30- 222. Count Complete Tree Nodes (Algo Academy) (easy) (algo: bfs but you can also do in dfs)  (time complexity O(n))

'''
222. Count Complete Tree Nodes
Easy
Topics
Companies Amazon Google Apple
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.

'''

# #Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         # 1- create a queue that is initialized with root
#         # 2- shift out from queue (this is our current node)
#         # 3- process node -increment a count (in this problem case)
#         # 4 push the current node children into the queue
#         #5- repeat steps 2-4 until queue is empty

#         queue = deque()
#         queue.append(root)
#         count = 0

#         while queue:
#             node = queue.popleft()

#             if node:
#                 count +=1
#                 queue.append(node.left)
#                 queue.append(node.right)
#         return count


# root1 = TreeNode(1)
# root1.left = TreeNode(2)
# root1.right = TreeNode(3)
# root1.left.left = TreeNode(4)
# root1.left.right = TreeNode(5)
# root1.right.left = TreeNode(6)
# sol = Solution()
# print(sol.countNodes(root1))


#! 31- 1046. Last Stone Weight (Algo Academy) (easy) (algo: heap)  (time complexity O(log(n)))
#! the most important part is to know when to use a heap the solution is not that hard
'''
1046. Last Stone Weight
Easy
Topics
Companies
Hint
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.(which mean second - first)
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.



Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1


Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

'''

# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:

#         stones = [-s for s in stones]
#         heapq.heapify(stones)
#         # print (stones)
#         while len(stones)>1:

#             first = heapq.heappop(stones)
#             second = heapq.heappop(stones)
#             if second > first:
#                 heapq.heappush(stones, first -second)

#         stones.append(0)
#         return abs(stones[0])

# '''
#                  -8
#                /    \
#               -7     -4
#              /  \   /  \
#            -1   -2 -1

# Overall, considering the most significant operation in
# the loop is heappop and heappush, the time complexity is
# dominated by the while loop and is approximately O(n log n),
# where n is the number of stones in the initial list.
# '''


# stones = [2,7,4,1,8,1] #1
# sol = Solution()
# print(sol.lastStoneWeight(stones))

#! 32- 1845. Seat Reservation Manager (Algo Academy) (Medium) (algo: heap)  (time complexity O(log(n)))

'''
1845. Seat Reservation Manager
Medium
Topics
Companies
Hint
Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve() Fetches the #!smallest-numbered unreserved seat,(b/c we are getting the smallest number every time we know we can solve it with a heap )
 reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.


Example 1:

Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].


Constraints:

1 <= n <= 105
1 <= seatNumber <= n
For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
For each call to unreserve, it is guaranteed that seatNumber will be reserved.
At most 105 calls in total will be made to reserve and unreserve.

'''

# class SeatManager:

#     def __init__(self, n: int):
#         self.unreserved =[i for i in range(1, n+1)]
#         # heapq.heapify(self.unreserved) we don't need this cause the list is already arranged with the range above


#     def reserve(self) -> int:
#         return heapq.heappop(self.unreserved)


#     def unreserve(self, seatNumber: int) -> None:
#         heapq.heappush(self.unreserved, seatNumber)



# # Your SeatManager object will be instantiated and called as such:
# # obj = SeatManager(n)
# # param_1 = obj.reserve()
# # obj.unreserve(seatNumber)

# # Test case
# seatManager = SeatManager(5)
# print(seatManager.reserve())    # Output should be 1
# print(seatManager.reserve())    # Output should be 2
# seatManager.unreserve(2)
# print(seatManager.reserve())    # Output should be 2
# print(seatManager.reserve())    # Output should be 3
# print(seatManager.reserve())    # Output should be 4
# print(seatManager.reserve())    # Output should be 5
# seatManager.unreserve(5)
# print(seatManager.reserve())    # Output should be 5


#! 33- 973. K Closest Points to Origin (Algo Academy) (Medium) (algo: heap)  (time complexity O(log(n)))

'''
973. K Closest Points to Origin
Medium
Topics
Companies Amazon Asana Facebook
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).



Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.


Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104

'''

# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         pts= []

#         for x,y in points:
#             # dist = math.sqrt(abs(x-0)**2 + abs(y-0)**2)
#             dist = abs(x-0)**2 + abs(y-0)**2
#             pts.append([dist,x,y])
#         res = []
#         heapq.heapify(pts)
#         # print (pts)

#         for i in range(k):
#             dist, x , y = heapq.heappop(pts)
#             res.append([x,y])

#         return res
# points = [[1,3],[-2,2]]
# k = 1


# # points = [[3,3],[5,-1],[-2,4]] # [[3,3],[-2,4]]
# # k = 2

# sol = Solution()
# print(sol.kClosest(points, k))


#! 34- 78. Subsets (Algo Academy) (Medium) (algo: backtracking)  (time complexity ???)

'''
78. Subsets
Medium
Topics
Companies
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

'''


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         ans = []
#         sub_set = []

#         def _backtrack(i):
#             # base case
#             if i >= len(nums):
#                 ans.append(sub_set.copy())
#                 print ('sub_set in base case #########', sub_set)
#                 print ('Done')

#                 return
#             #Decision to include nums[i]
#             sub_set.append(nums[i])
#             print('nums[i]======>', nums[i])
#             _backtrack(i+1)
#             sub_set.pop()
#             print ('sub_set---------------------------->', sub_set)
#             # Decision to exclude nums[i]
#             _backtrack(i+1)
#         _backtrack(0)
#         return ans

# nums = [1,2,3]
# sol = Solution()
# print(sol.subsets(nums))


#! 35- 22. Generate Parentheses (Medium) (algo: backtracking)  (time complexity exponent)

'''
22. Generate Parentheses
Medium
Topics
Companies Amazon Microsoft TikTok
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
'''

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = []
#         res = []

#         def _backtrack(openN, closedN):
#             if openN == closedN == n:
#                 res.append("".join(stack)) # here we created a string to add to res
#                 return
#             if openN < n:
#                 # print (openN ,"^1^", closedN)
#                 stack.append("(")
#                 _backtrack(openN +1, closedN)
#                 stack.pop() # if we remove this it will keep adding parentheses

#             if closedN < openN:
#                 # print (openN, "*2*", closedN)
#                 stack.append(")")
#                 _backtrack(openN, closedN +1)
#                 stack.pop() # if we remove this it will keep adding parentheses

#         _backtrack(0,0)
#         return res
'''
n is total num of parentheses we don't want open ( to exceed it
we also don't want closed ) to exceed open ( . Remember it said in the
question "well-formed parentheses." and "pairs of parentheses"
'''
# #! a faster solution from leet code
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#             def backtrack(parenthesis, opened, closed):
#                 # save solution
#                 if len(parenthesis) == 2*n:
#                     res.append(parenthesis)
#                 # add opened parenthesis
#                 if opened < n:
#                     backtrack(parenthesis + "(", opened+1, closed)
#                 # add closed parenthesis
#                 if closed < opened:
#                     backtrack(parenthesis + ")", opened, closed+1)

#             res = []
#             backtrack("", 0, 0)
#             return res
# '''
#     this solution is much faster cause it uses a string not a stack/list
#     the base case is also faster
#     also recursion only for the number of open parentheses
#     there is no backtracking here
# '''


# n = 3
# sol = Solution()
# print(sol.generateParenthesis(n))

#! 36- 79. Word Search (Medium) (algo: backtracking)  (time complexity O(R*C*4**s))
'''
79. Word Search
Medium
Topics
Companies Bloomberg Uber TikTok
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


'''
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         # base cases
#         #1.if we find the word we return true
#         #   a. keep track of index done when i == len(word)
#         #2. return false
#         #    a.when we are out of bounds
#         #    b. letter does not match with the word[i]
#         #    c.we have visited
#         ROWS , COLS = len(board), len(board[0])
#         visited = set()
#         ##############################################
#         def backtrack(r,c,i):
#             #base cases
#             if i == len(word):
#                 return True
#             if not inbound(r,c) or word[i] != board[r][c] or (r,c)in visited:
#                 return False

#             # modify
#             visited.add((r,c))
#             print ('row and columns', (r,c))

#              # recursion
#             res = (backtrack(r+1, c, i+1) or
#             backtrack(r-1, c, i+1) or
#             backtrack(r, c+1, i+1) or
#             backtrack(r, c-1, i+1))

#             #backtrack
#             print ('discard row and columns ==============', (r,c))
#             visited.discard((r,c))

#             return res
#         ###############################################
#         def inbound (r,c):
#             rowInbound = r >= 0 and r < ROWS
#             colInbound = c >= 0 and c < COLS
#             return rowInbound and colInbound
#         ###############################################
#         for r in range (ROWS):
#             for c in range(COLS):
#                 if backtrack(r,c,0):
#                     return True
#         return False


# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# sol = Solution()
# print(sol.exist(board, word))

#! 37- 380. Insert Delete GetRandom O(1) (Medium) (algo: design problem)  (time complexity O(1))

'''
380. Insert Delete GetRandom O(1)
Medium
Topics
Companies Bloomberg Amazon Google
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.



Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.

'''


# class RandomizedSet:

#     def __init__(self):
#         self.map = {}
#         self.list =[]


#     def insert(self, val: int) -> bool:
#         # print ('value ===========>',val)
#         if val in self.map:
#             return False
#         self.list.append(val)
#         # print ('list ******', self.list)
#         self.map[val] = len(self.list)-1
#         # print ('map is ++++++++++++++',self.map)
#          # key value pair with index as the value
#         return True


#     def remove(self, val: int) -> bool:
#         if val not in self.map:
#             return False
#         # swamp element in list
#         lastElement , idx = self.list[-1], self.map[val]
#         print ('list ******', self.list)
#         print ( 'lastElement=======' , lastElement)
#         print ('map is ++++++++++++++',self.map)
#         print ('self.map[val]*************', self.map[val])
#         self.list[idx], self.map[lastElement] = lastElement, idx
#         print ('____________________________')
#         print ('list ******', self.list)
#         print ( 'lastElement=======' , lastElement)
#         print ('map is ++++++++++++++',self.map)
#         print ('self.map[val]*************', self.map[val])
#         #pop from list
#         print (' before pop list is ==' , self.list)
#         self.list.pop()
#         print (' now after the pop list is ==' , self.list)
#         print ('map is ++++++++++++++',self.map)
#         # update map

#         del self.map[val]
#         print ('map is ^^^^^^^^^^^',self.map)
#         return True


#     def getRandom(self) -> int:
#         return random.choice(self.list)



# randomizedSet = RandomizedSet()
# print(randomizedSet.insert(1))  # Inserts 1 to the set. Returns true as 1 was inserted successfully.
# print(randomizedSet.remove(2))  # Returns false as 2 does not exist in the set.
# print(randomizedSet.insert(2))  # Inserts 2 to the set, returns true. Set now contains [1,2].
# print(randomizedSet.insert(3))  # 2 was already in the set, so return false.
# print(randomizedSet.getRandom())  # getRandom() should return either 1 or 2 randomly.
# print(randomizedSet.remove(1))  # Removes 1 from the set, returns true. Set now contains [2].
# print(randomizedSet.insert(2))  # 2 was already in the set, so return false.
# print(randomizedSet.getRandom())  # Since 2 is the only number in the set, getRandom() will always return 2.

'''
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
'''

#! 35-146. LRU Cache (Medium) (algo: design problem)  (time complexity O(1))

'''
146. LRU Cache
Medium
Topics
Companies Amazon DoorDash Bloomberg
Design a data structure that follows the constraints of a #!Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

'''

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.dll =DoubleLinkedList() # creates only one double linked list # there is only one instance of double linked list
#         self.hash = {}



#     def get(self, key: int) -> int:
#         if key not in self.hash:
#             return -1
#         # 1-remove if in dll to re-position
#         self.dll.remove(self.hash[key]) # why remove from dll? to place again at the end to indicate it is most recently used
#         # 2- add to the new position in dll and update the hash
#         self.hash[key] = self.dll.push(self.hash[key]) # why? updating the position of the node in hash and add it to dll
#         # print ('hash is ',self.hash[key])
#         return self.hash[key].val



#     def put(self, key: int, value: int) -> None:

#         # 1-remove the node if exists in dll
#         if key in self.hash:
#             self.dll.remove(self.hash[key]) # why? cause we want to put the node which the value of the key near the tail

#         # 2-add the new node
#         newNode = Node(key,value) # create the new node
#         self.hash[key]= self.dll.push(newNode) #  form the push() it returned the new node with new next and prev
#         # the node is connected to the double linked list through the next and prev attributes

#         #3-# remove the lru
#         if self.dll.length > self.capacity:
#             lru = self.dll.head.next # cause head is dummy
#             del self.hash[lru.key] # remove lru from hash too
#             self.dll.remove(lru) # remove lru from dll
#         # print ('hash is ',self.hash) you can't print it you need to iterate over it to print the nodes




# class Node:
#     def __init__(self,key, val):
#         self.key = key
#         self.val = val
#         self.next = None
#         self.prev = None
#     # def __str__(self):
#     #     return f"Node({self.key}, {self.val})" # this is override printing the node to show key and val in stead of memory address
# class DoubleLinkedList:

#     def __init__(self):
#         self.head = Node(None, None)
#         self.tail = Node(None, None)
#         self.head.next = self.tail
#         self.tail.prev =self.head

#         self.length = 0
#         # print ('self is', self)

#     def remove(self, node):
#         prev =node.prev
#         nxt = node.next
#         # print("Doubly Linked List before decrementing length:")
#         # self.print_list()

#         prev.next = nxt
#         nxt.prev = prev

#         self.length -= 1
#         # print("Doubly Linked List after decrementing length:")
#         # self.print_list()

#     def push(self,node):
#         prev = self.tail.prev
#         nxt = self.tail
#         # print("Doubly Linked List before incrementing length:")
#         # self.print_list()

#         prev.next = node
#         nxt.prev = node

#         node.next = nxt
#         node.prev = prev

#         self.length +=1
#         # print("Doubly Linked List after incrementing length:")
#         # self.print_list()
#         # print ('node key is ==>', node.key,'node val is ==>', node.val)
#         # print ( 'this is the put node' , node)

#         return node #! what is this node returned? is it the linked list? it is the node with attribures next and prev



#     def print_list(self):
#         current =self.head
#         values = []
#         while current != self.tail:
#             if current.key is not None and current.val is not None:
#                 values.append(f"({current.key}, {current.val})")
#             current = current.next
#         print ("double linked list:"+"<->".join(values))






# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)

#     # Instantiate the LRUCache object with capacity 2
# cache = LRUCache(2)

# # Perform operations as specified in the input
# print(cache.put(1, 1))  # Put key=1, value=1
# print(cache.put(2, 2))  # Put key=2, value=2
# print(cache.get(1))     # Get value associated with key=1 (Expected output: 1)
# print(cache.put(3, 3))  # Put key=3, value=3
# print(cache.get(2))     # Get value associated with key=2 (Expected output: -1, as key 2 was evicted by key 3)
# print(cache.put(4, 4))  # Put key=4, value=4
# print(cache.get(1))     # Get value associated with key=1 (Expected output: -1, as key 1 was evicted by key 4)
# print(cache.get(3))     # Get value associated with key=3 (Expected output: 3)
# print(cache.get(4))     # Get value associated with key=4 (Expected output: 4)

#! 36- 200. Number of Islands (Medium) (algo: matrix dfs)  (time complexity O(ROWS * COLS))

'''
200. Number of Islands
Medium
Topics
Companies Amazon Bloomberg Google
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''


# class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
        ######################################################
        # #!helper function to traverse
        # def _dfs(row,col):
        #     if not _inbound(row,col): # check if out of bound
        #         return False
        #     pos = f'{row}, {col}'

        #     if pos in visited: # check if in visited
        #         return False

        #     if grid[row][col] =='0': # check if an island
        #         return False
        #     visited.add(pos)

        #     directions = ((1,0),(0,1),(-1,0),(0,-1))
        #     #! what the fuck is this? how many recursions do we have?
        #     for dir in directions:
        #         # print ("dir is ",dir)
        #         newRow = row+dir[0]
        #         # print ('new row' , newRow)
        #         newCol = col+dir[1]
        #         _dfs(newRow,newCol)
        #     return True
        # ####################################################
        # #! helper function to check inbound
        # def _inbound(row,col):
        #     rowInbound = 0 <= row and row < len(grid)
        #     colInbound = 0 <= col and col < len(grid[0])
        #     return rowInbound and colInbound
        # count = 0
        # visited = set()
        # #! find th coordinates and recursion
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if _dfs(row,col):
        #             count+=1
        # print (visited)
        # return count
#! fastest code
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         count = 0
#         ROWS = len(grid)
#         COLS = len(grid[0])

#         def dfs(r, c):
#             if c < 0 or r < 0 or c >= COLS or r >= ROWS:
#                 return
#             if grid[r][c] == "0":
#                 return

#             grid[r][c] = "0"

#             dfs(r - 1, c)
#             dfs(r + 1, c)
#             dfs(r, c - 1)
#             dfs(r, c + 1)

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == "1":
#                     count += 1
#                     dfs(r, c)

#         print (grid)
#         return count



# # grid = [
# #   ["1","1","1","1","0"],
# #   ["1","1","0","1","0"],
# #   ["1","1","0","0","0"],
# #   ["0","0","0","0","0"]
# # ]
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# sol = Solution()
# print(sol.numIslands(grid))


#! 37- 695. Max Area of Island (Medium) (algo: matrix dfs)  (time complexity O(ROWS * COLS))

'''
695. Max Area of Island
Medium
Topics
Companies Amazon bloomberg facebook
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

'''

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         # base cases
#         # 1-is it inbound
#         # 2-is the value 0
#         # 3-has the cell been visited

#         rows, cols = len(grid), len(grid[0])

#         def dfs(r,c):
#             if not inbound(r,c) or grid[r][c] ==0:
#                 return 0
#             pos = (r,c)
#             if pos in visited:
#                 return 0
#             size = 1
#             visited.add(pos)

#             directions = ((1,0),(0,1),(-1,0),(0,-1))
#             for dir in directions:
#                 newRow = r + dir[0]
#                 newCol = c + dir[1]
#                 size += dfs(newRow, newCol)
#             return size


#         def inbound(r,c):
#             rowInbound = 0 <= r < rows
#             colInbound = 0 <= c < cols
#             return rowInbound and colInbound

#         largestIsland = 0
#         visited = set()
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:
#                   largestIsland = max(largestIsland, dfs(r,c))

#         return largestIsland

    #! another faster solution

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         max_row, max_col = len(grid), len(grid[0])
#         max_area = 0

#         def find_max_area(r, c):
#             nonlocal max_row, max_col, max_area
#             if r < 0 or r >= max_row or c < 0 or c >= max_col:
#                 return 0

#             if grid[r][c] == 0:
#                 return 0

#             grid[r][c] = 0
#             return 1 + find_max_area(r+1, c) + find_max_area(r-1, c) + find_max_area(r, c+1) + find_max_area(r, c-1)


#         for r in range(max_row):
#             for c in range(max_col):
#                 if grid[r][c] == 1:
#                     max_area = max(max_area, find_max_area(r, c))

#         return max_area


# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,1,1,0,1,0,0,0,0,0,0,0,0],
#         [0,1,0,0,1,1,0,0,1,0,1,0,0],
#         [0,1,0,0,1,1,0,0,1,1,1,0,0],
#         [0,0,0,0,0,0,0,0,0,0,1,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# sol = Solution()
# print(sol.maxAreaOfIsland(grid))

 #!  38-417. Pacific Atlantic Water Flow (Medium) (algo: matrix dfs)  (time complexity O(ROWS * COLS))
'''
417. Pacific Atlantic Water Flow
Medium
Topics
Companies Google Amazon Bloomberg
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.



Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105



'''
# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         rows, cols = len(heights), len(heights[0])
# # traverse helper function and base cases
#         def dfs(r,c,visited,prevHeight):

#             # print ('prevHeight=================', prevHeight  )
#             # print ('heights[r][c]', heights[r][c] if inbound (r,c) else None)

#             if (r,c) in visited or not inbound(r,c) or heights[r][c]< prevHeight:
#                 return
#             visited.add((r,c))
#              # check directions
#             directions = ((1,0),(0,1),(-1,0),(0,-1))
#             for dir in directions:
#                 newRow = r + dir[0]
#                 newCol = c + dir[1]
#                 dfs(newRow,newCol,visited,heights[r][c]) #! this is where we get the prev hight
#         # check inbound
#         def inbound(r,c):
#             rowInbound = 0 <= r < rows
#             colInbound = 0 <= c < cols
#             return rowInbound and colInbound
# #################################################################
#         res = []
#         pacific = set()
#         atlantic = set()
# # check the columns
#         for c in range(cols):
#             # print ('start the north traverse ************************************************************')
#             #first row (north)
#             # print ('columns' ,heights[0][c])
#             # print ('pacific', pacific)
#             dfs(0,c,pacific,heights[0][c]) #! puts the tuples in pacific

#             #last row (south)
#             # print ('atlantic',atlantic)
#             # print ('rows' ,heights[rows-1][c])
#             dfs(rows-1,c,atlantic,heights[rows-1][c]) #! puts the tuples in atlantic
#         # print ('atlantic',atlantic)
# ###############################################################
# # check the rows
#         for r in range(rows):
#             #first row (west)
#             # print ('rows' ,heights[r][0])
#             dfs(r,0,pacific,heights[r][0])
#             #last row (east)
#             dfs(r,cols-1,atlantic,heights[r][cols-1])
#         # print ('atlantic22222',atlantic)

# #############################################################

# # coordinates and do what you need to do
#         for r in range(rows):
#             for c in range(cols):
#                 if (r,c) in pacific and (r,c) in atlantic:
#                     res.append([r,c])
#         return res


# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# sol = Solution()
# print(sol.pacificAtlantic(heights))


#! 39-1091. Shortest Path in Binary Matrix (Medium) (algo: matrix bfs)  (time complexity ???))
'''
1091. Shortest Path in Binary Matrix
Medium
Topics
Companies = Facebook Amazon Google
Hint
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''


# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         rows , cols = len(grid), len(grid[0])
#         if grid[0][0] ==1 or grid[rows-1][cols-1] ==1:
#             return -1
#         # 1. Initialize the queue with starting value(s)
#         # 2.pop current node from queue
#         # 3.process current node
#         # 4.push neighbors into queue if they are valid
#         # 5.repeat steps 2-4 until queue is empty
#         def inbound(r,c):
#             rowInbound = 0 <= r < rows
#             colInbound = 0 <= c < cols
#             return rowInbound and colInbound

#         queue = deque()
#         queue.append((0,0,1)) #(r,c,layer)
#         directions = ((1,0),(0,1),(-1,0),(0,-1),(1,1), (1,-1),(-1,1), (-1,-1))
#         visited = set()
#         visited.add((0,0))
#         print ('queue start',queue)


#         while queue:
#             row,col, level = queue.popleft() # destructure
#             print('level', level )
#             if row == rows-1 and col == cols-1:
#                 return level

#             for dir in directions:
#                 newRow = row+ dir[0]
#                 newCol = col + dir[1]

#                 if inbound(newRow, newCol) and grid[newRow][newCol] != 1 and (newRow, newCol) not in visited:
#                     print ('newrow , newcol', newRow,newCol)
#                     queue.append((newRow,newCol,level+1))
#                     print (queue)
#                     visited.add((newRow,newCol))

#         return -1






# grid = [[0,0,0],[1,1,0],[1,1,0]] # 4
# sol = Solution()
# print(sol.shortestPathBinaryMatrix(grid))

#! 40- 994. Rotting Oranges  (Medium) (algo: matrix bfs)  (time complexity ???))

'''
994. Rotting Oranges
Medium
Topics
Companies Amazon Lyft Adobe
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

'''

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         rows , cols = len(grid) , len(grid[0])

#         def inbound(r,c):
#             rowInbound = 0 <= r < rows
#             colInbound = 0 <= c < cols
#             return rowInbound and colInbound
#         queue = deque()
#         freshOranges = 0
#         time = 0

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] ==1 :
#                     freshOranges +=1
#                 elif grid[r][c] ==2:
#                     queue.append((r,c,0)) #! new starting point
#         print (queue)
#         print('fresh oranges No =',freshOranges)

#         directions = ((1,0),(0,1),(-1,0),(0,-1))
#         while queue:
#             r,c, level = queue.popleft() # don't forget level becomes zero again
#             time = level
#             for dir in directions:
#                 newRow = r + dir[0]
#                 newCol = c + dir[1]

#                 if inbound(newRow,newCol) and grid[newRow][newCol] == 1:
#                     queue.append((newRow,newCol,level+1))
#                     print('queue ========',queue)
#                     grid[newRow][newCol] = 2
#                     freshOranges -= 1
#         return time if freshOranges == 0 else -1


# grid = [[2,1,1],[1,1,0],[0,1,1]] # 4
# grid = [[2,1,1],[2,1,0],[0,1,1]] # 3 # it takes them in pairs cause there are more than one starting node here

# sol = Solution()
# print(sol.orangesRotting(grid))


#! 41- 542. 01 Matrix (Medium) (algo: matrix bfs)  (time complexity ???))

'''
542. 01 Matrix
Medium
Topics
Companies Amazon Google Bloomberg
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
'''
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         rows , cols = len(mat) , len(mat[0])
#         directions = ((1,0),(0,1),(-1,0),(0,-1))


#         def inbound(r,c):
#             rowInbound = 0 <= r < rows
#             colInbound = 0 <= c < cols
#             return rowInbound and colInbound
#         queue = deque()
#         for r in range(rows):
#             for c in range(cols):
#                 if mat[r][c] == 0:
#                     queue.append((r,c)) # add starting points
#                 else:
#                     mat[r][c] = -1  # to mark the visited ones later
#         print ('queue===========', queue)
#         while queue:
#             r,c = queue.popleft()

#             for dir in directions:
#                 newRow = r + dir[0]
#                 newCol = c + dir[1]

#                 # print ('mat is **** before', mat)
#                 if not inbound(newRow,newCol) or mat[newRow][newCol] != -1: continue # move to next iteration if true
#                 mat[newRow][newCol] = mat [r][c] +1 # just notice that it is the adjacent one r c
#                 print ('mat  is ====', mat)
#                 queue.append((newRow,newCol))

#         return mat
    #! faster solution

    # rows,cols = len(mat), len(mat[0])
    #     directions = ((0,1),(1,0),(0,-1),(-1,0))

    #     m, n = len(mat), len(mat[0])

    #     for r in range(m):
    #         for c in range(n):
    #             if mat[r][c] > 0:
    #                 top = mat[r - 1][c] if r > 0 else math.inf
    #                 left = mat[r][c - 1] if c > 0 else math.inf
    #                 print ('mat====>', mat)
    #                 mat[r][c] = min(top, left) + 1
    #                 print (min(top, left))

    #     for r in range(m - 1, -1, -1):
    #         for c in range(n - 1, -1, -1):
    #             if mat[r][c] > 0:
    #                 bottom = mat[r + 1][c] if r < m - 1 else math.inf
    #                 right = mat[r][c + 1] if c < n - 1 else math.inf
    #                 mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
    #     return mat



# mat = [[0,0,0],[0,1,0],[0,0,0]] # [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# mat = [[0,0,0],[0,1,0],[1,1,1]] #[[0,0,0],[0,1,0],[1,2,1]]
# sol = Solution()
# print(sol.updateMatrix(mat))


#! 41- 797. All Paths From Source to Target (Medium) (algo: adjacency list, dfs , backtracking)  (time complexity ???))

'''
797. All Paths From Source to Target
Medium
Topics
Companies Google Bloomberg Adobe
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).



Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.

'''
# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         target = len(graph) -1 #3
#         results =[]
#         # you back track to go again the other way
#         def backtrack(currentNode, path): #0 , [0]
#             if currentNode == target:
#                 results.append(list(path))
#                 return

#             for neighbor in graph[currentNode]:
#                 # print ('graph current node ',graph[currentNode]) # [1,2] # [3]
#                 # print('path before', path) # [0] # [0,1]
#                 path.append(neighbor)
#                 print ('neighbor is ===>',neighbor) #1 # 3 # None
#                 # print ('path middle', path) #[0,1] [0,1,3]
#                 backtrack(neighbor,path)
#                 print ('path end', path) # nothing # [0,1,3] then [0,1] #
#                 path.pop()
#                 # print (' path ****',path)

#         path = [0]
#         backtrack(0,path)

#         return results

# '''
# 0 --> 1
# |     |
# v     v
# 2 --> 3

# '''
# graph = [[1,2],[3],[3],[]] # [[0, 1, 3], [0, 2, 3]]

# sol = Solution()
# print(sol.allPathsSourceTarget(graph))

#! 42- 1129. Shortest Path with Alternating Colors (Medium) (algo: adjacency list, bfs)  (time complexity ???))

'''
1129. Shortest Path with Alternating Colors
Medium
Topics
Companies Bloomberg linkedin Google
Hint
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.



Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]


Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n

'''

# class Solution:
#     def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
#         red = defaultdict(list)
#         blue = defaultdict(list)

#         for src , dst in redEdges:
#             red[src].append(dst) # we use append cause it is a list in the defaultdict we can use assignment [] = dst for the first value only
#         for src, dst in blueEdges:
#             blue[src].append(dst)
#         # print ('red=========' , red)
#         # print ('blue',blue)

#         #initialize queue with starting node
#         answer = [-1 for _ in range(n)]
#         queue = deque([(0,0,None)]) # (node,length, prev_edge, color)   #! why do we have tuple and list
#         visited = set([(0,None)])

#         while queue:
#             # shift current node out from queue
#             node, length , edgeColor = queue.popleft()
#             #process node
#             if answer[node] == -1:
#                 answer[node] = length # replace it with the length

#             #push all valid neighbors into queue
#             if edgeColor != 'RED': # we use not because we start with 'None' # if the previous node popped off is not red then the code starts exploring the red list
#                 for neighbor in red[node]: # we check the red list , this check the val of the key
#                     if (neighbor, 'RED') not in visited:
#                         visited.add((neighbor,'RED'))
#                         queue.append((neighbor,length+1, 'RED'))
#             if edgeColor != 'BLUE':
#                 for neighbor in blue[node]:
#                     if (neighbor, 'BLUE') not in visited:
#                         visited.add((neighbor,'BLUE'))
#                         queue.append((neighbor,length+1, 'BLUE'))

#         print ('visited', visited)
#         return answer


# n = 3
# redEdges = [[0,1],[1,2]] #[0,1,-1]
# blueEdges = []
# sol = Solution()
# print(sol.shortestAlternatingPaths(n,redEdges,blueEdges))

#! 43- 785. Is Graph Bipartite? (Medium) (algo: adjacency list , dfs)  (time complexity ???))

'''
785. Is Graph Bipartite?
Medium
Topics
Companies TikTok Apple Amazon
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.



Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

'''
# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         nodeColors = {}
#         LEN = len(graph)

#         def colorNodes(node, currentColor):
#             if node in nodeColors:
#                 return nodeColors[node] == currentColor
#             nodeColors[node] = currentColor
#             for neighbor in graph[node]:
#                 if not colorNodes(neighbor,not currentColor):
#                     return False
#             return True
#         for node in range(LEN):

#             if node not in nodeColors and not colorNodes(node,True):
#                 # print ('nodeColors at the end if it is false', nodeColors)
#                 return False

#         # print ('nodeColors at the end if it is true', nodeColors)
#         return True

# #! with full explanation

# # class Solution:
# #     def isBipartite(self, graph: List[List[int]]) -> bool:
# #        nodeColors = {}
# #        print ('nodeColors', nodeColors) #{}

# # ##########################################################################
# #        def colorNodes(node, currentColor): # recursive function
# #            print ('node ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', node)
# #            if node in nodeColors: # Check if the node is already colored
# #                print ('node in nodeColors #####',node)
# #                print ('nodeColors[node] == currentColor =>$$$$$$$$$$',nodeColors[node] == currentColor)
# #                print (f'nodeColors[node]=, {nodeColors[node]} , currentColor is = {currentColor}')

# #                return nodeColors[node] == currentColor # Check if the color matches
# #            nodeColors[node] = currentColor # if node not in nodeColors then Color the current node with the given color
# #            print ('nodeColors after nodeColors[node] = currentColor!!!!!!', nodeColors)
# #            print ('nodeColors[node]==== ', nodeColors[node] )
# #            print('currentColor *****', currentColor  )

# #            for neighbor in graph[node]: #! second iteration through the node and neighboring nodes
# #                if not colorNodes(neighbor,not currentColor): # if colorNodes returns false it will be not False (True) then this condition will apply
# #                # if not (True) it means this condition is false thus not applicable
# #                    return False
# #            return True
# # ##########################################################################
# #        #! execution start
# #        for node in range(len(graph)): #! first iteration through all the nodes
# #            print ('===========================================>>>>>>>>>>>>>>>>>>START AGAIN')
# #            #Checks if the node is not already colored and colors it with True (considering it as part of set A).
# #            print(f'loop == {node}')
# #            if node not in nodeColors and not colorNodes(node,True): #! why does it have to be true and red is not working?
# #                return False
# #        print ('nodeColors at the end', nodeColors)
# #        return  True



# graph = [[1,2,3],[0,2],[0,1,3],[0,2]] # False
# # graph = [[1,3],[0,2],[1,3],[0,2]] #True
# sol = Solution()
# print(sol.isBipartite(graph))

#! 44- 509. Fibonacci Number (Algo Academy) (easy) (Tech: Dynamic Programming)  (Time Complexity O(n))


'''
509. Fibonacci Number
Easy
Topics
Companies
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).



Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Constraints:

0 <= n <= 30

'''

# class Solution:
#     def fib(self, n: int, memo ={}) -> int: # this is depth fist search

#         if n == 0 : return 0
#         if n == 1 : return 1
#         if n in memo: return memo[n]

#         memo[n]= self.fib(n-1,memo)+ self.fib(n-2, memo)
#         return memo[n]

# #! Fastest solution
# class Solution:
#     def fib(self, n: int, mono = {}) -> int:
#         if n==0: return 0
#         elif n==1 or n==2: return 1

#         else:
#             x=[0,1]
#             o=2
#             while o<n:
#                 x.append(x[o-1]+x[o-2])
#                 o=o+1

#             # print('X at the end == ',x)
#             return x[n-1]+x[n-2]



# n = 10
# solution = Solution()
# output = solution.fib(n)
# print(output)


#! 45 - 62. Unique Paths (Algo Academy) (medium) (Tech: dynamic programming, dfs)  (time complexity O(n) )
'''
62. Unique Paths
Medium
Topics
Companies
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:

1 <= m, n <= 100

'''

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         memo = {}
#         def pathCount(m,n):
#             if n == 0 or m == 0: return 0
#             if n == 1 and m == 1: return 1
#             key = f'{m},{n}'
#             if key in memo: return memo[key]
#             memo[key]= pathCount(m-1,n)+ pathCount(m, n-1)
#             return memo[key]
#         return pathCount(m,n)


    #! fastest solution
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         table = [[1 for _ in range(n)] for _ in range(m)] # creates a 2D list (or matrix) # [[1, 1], [1, 1], [1, 1]] representing rows and cols
#         # print (table) # [[1, 1], [1, 2], [1, 3]] # first row and the first column are already initialized
#         for i in range(1,m): #stop value is excluded
#             for j in range(1,n):
#                 table[i][j] = table[i-1][j]+ table[i][j-1]
#                 # replacing the value in the table with the values from going once right and once down or both this way we will find all the possible paths
#                 # Each cell stores the number of unique paths to reach it by summing up the number of
#                 #paths from the cell above and the cell to the left.
#                 #This calculation is based on the fact that to reach cell (i, j),
#                 #you can either come from above (i-1, j) or from the left (i, j-1)
#                 print ('i is ===',i)
#                 print ('j is ********',j)
#                 print (table[i][j])
#         print (table)
#         return table[m-1][n-1]
'''
it starts finding the paths from the bottom because of the recursion and goes to  0,0 to find the paths
it can be 0,0 and target be m-1 , n-1 or it can be 1,1 and m and n when you draw the grid.
this solution didn't pass on leet code because it is too slow there is another dynamic programming solution that is better.
'''
# m = 3
# n = 2

# solution = Solution()
# output = solution.uniquePaths(m,n)
# print(output)

#! 46 - 70. Climbing Stairs (Algo Academy) (medium) (Tech: dynamic programming, dfs)  (time complexity O(n) )

'''
70. Climbing Stairs
Easy
Topics
Companies Amazon Apple Uber
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45

'''



# class Solution:
#     def climbStairs(self, n: int, memo ={}) -> int:
#         if n ==1: return 1
#         if n == 2: return 2
#         if n in memo: return memo[n]

#         memo[n] = self.climbStairs(n-1,memo)+ self.climbStairs(n-2,memo)
#         return memo[n]





# n = 3

# solution = Solution()
# output = solution.climbStairs(n)
# print(output)

#! 47 - 322. Coin Changes (Algo Academy) (medium) (Tech: dynamic programming)  (time complexity O(n) )

'''
322. Coin Change
Medium
Topics
Companies Apple Bloomberg  Mathworks
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(rem,memo):
            if rem == 0: return 0
            if rem in memo: return memo[rem]

            memo[rem]= float("inf")
            print (memo)

            for coin in coins:
                print('coin is =',coin)
                if rem - coin >= 0:
                    memo[rem] = min (memo[rem], dfs(rem - coin, memo) +1)
                    print (memo)
            return memo[rem]


        memo = defaultdict(int)
        print (memo)
        result = dfs(amount, memo)
        return result if result != float("inf") else -1


coins = [1,2,5] #3
# amount = 11
amount = 6
solution = Solution()
output = solution.coinChange(coins, amount)
print(output)

#! 11-752. Open the Lock -(Lecture) - (Medium)
#! 12-554. Brick Wall -(Lecture) - (Medium)
#! 13-51. N-Queens -(Lecture)- (Hard)



#! 10-1376. Time Needed to Inform All Employees -(Lecture) - (Medium)

'''
1376. Time Needed to Inform All Employees
Medium
Topics
Companies
Hint
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.



Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
Example 2:


Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.


Constraints:

1 <= n <= 105
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.

'''
