import math
import os
import random
import re
import sys

#! 1-

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

print(plusMinus(arr))

#! Chat Gpt solutions

def plusMinus(arr):

    #! solution 1
    n = len(arr)
    # positive_count = sum(1 for num in arr if num > 0) # 1 is a place holder 
    # negative_count = sum(1 for num in arr if num < 0)
    # zero_count = n - positive_count - negative_count
    #! solution 2

    positive_count = sum( num > 0 for num in arr)
    negative_count = sum (num < 0 for num in arr)
    zero_count = n - positive_count - negative_count


    positive_ratio = positive_count / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n

    # Print the ratios with 6 decimal places
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))

# Example usage:
arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
