import math
import os
import random
import re
import sys
from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random

#! 1- Plus Minus

'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .

Constraints

0<n<= 100
-100<arr[i]<= 100
Output Format

Print the following  lines, each to  decimals:

proportion of positive values
proportion of negative values
proportion of zeros
Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: 3/6 = 0.500000,
negative:2/6=0.333333  and zeros: 0.166667


'''




#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#!my solution
# def plusMinus(arr):
#     qty = []
#     qty1 =[]
#     qty2 = []


#     for number in (arr):
#         if number == 0:
#             qty.append(number)
#         elif number > 0:
#              qty1.append(number)
#         else:
#             qty2.append(number)


#     more = len(qty1)/len(arr)
#     less = len(qty2)/len(arr)
#     equal = len(qty)/len(arr)
#     result = f"{more:.6f}\n{less:.6f}\n{equal:.6f}\n"

#     # return result
#     print(result)

# # arr = [1,1,0,-1,-1]
# arr = [-4, 3, -9, 0, 4, 1]

# print(plusMinus(arr))

# #! Chat Gpt solutions

# def plusMinus(arr):

#     #! solution 1
#     n = len(arr)
#     # positive_count = sum(1 for num in arr if num > 0) # 1 is a place holder
#     # negative_count = sum(1 for num in arr if num < 0)
#     # zero_count = n - positive_count - negative_count
#     #! solution 2

#     positive_count = sum( num > 0 for num in arr)
#     negative_count = sum (num < 0 for num in arr)
#     zero_count = n - positive_count - negative_count


#     positive_ratio = positive_count / n
#     negative_ratio = negative_count / n
#     zero_ratio = zero_count / n

#     # Print the ratios with 6 decimal places
#     print("{:.6f}".format(positive_ratio))
#     print("{:.6f}".format(negative_ratio))
#     print("{:.6f}".format(zero_ratio))

# # Example usage:
# arr = [-4, 3, -9, 0, 4, 1]
# plusMinus(arr)



#! 2-Mini-Max Sum

'''
1- iterate over the list add the numbers except for one number
iterate and remove one number every time you can have an i and increment it to remove the next number
we need an array to collect the numbers and then we return the max and min in that array using min and max
we can deduct the value of item at i after adding everything in the arr
'''


#!

'''
Given five positive integers, find the minimum and maximum values that can be calculated by
summing exactly four of the five integers. Then print the respective minimum and maximum
values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

Input Format

A single line of five space-separated integers.

Constraints

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14

'''

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# arr = [1,3,5,7,9]
# def miniMaxSum(arr):
    # nums = []

    # total = sum(arr)
    # # print (total)
    # for n in arr:
    #     number = total - n
    #     nums.append(number)

    # max1 = max(nums)
    # min1 = min(nums)
    # print (min1, max1)
    # Write your code here

    #! another solution (GPT)

#     total_sum = sum(arr)
#     min_sum = total_sum - max(arr)
#     max_sum = total_sum - min(arr)

#     print(min_sum, max_sum)

# # if __name__ == '__main__':

# #     arr = list(map(int, input().rstrip().split()))

# miniMaxSum(arr)


#! Sparse Arrays

# def matchingStrings(strings, queries):
#     #! O(n*2) solution
#     res1 = []


#     for query in queries:
#         counter = 0
#         for string in strings:
#             if string == query:
#                 counter +=1
#         res1.append(counter)


#     return res1

#     # count = Counter(strings)

#     #! o(n) solution

#     # res = [count[query] for query in queries]

#     # return res




# strings = ["aba"
#     , "baba"
#     , "aba"
#     , "xzxb"]

# queries = [
#     "aba"
#     , "xzxb"
#     , "ab"
# ]
# print (matchingStrings(strings,queries))


def lonelyInteger(a):


    # solution one
        count = Counter(a)
        for number in count:
            if count[number] == 1:
                return number
    #solution two

str = [1, 2, 3, 4, 3, 2, 1]  # output 2

print(lonelyInteger(str))

'''
You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and return the result as an unsigned integer.

Example

. We're working with 32 bits, so:



Return .

Function Description

Complete the flippingBits function in the editor below.

flippingBits has the following parameter(s):

int n: an integer
Returns



'''
