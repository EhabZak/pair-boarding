from typing import List

#! third mock interview

#! 1- 575. Distribute Candies


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

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = set(candyType)
        length = len(candyType)

        sLen = len(s)

        return min(length, sLen)


candyType = [1,1,2,2,3,3] #3
candyType = [6,6,6,6] #1


solution = Solution()
output = solution.distributeCandies(candyType)
print(output)

#! 2- problem 1. Two Sum

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
