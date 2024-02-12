
from collections import Counter,defaultdict
#! IBM questions /////////////////

#! 1- find HCF (Highest Common Factor) (alog: Euclidean algorithm)
'''

Write a program to find HCF of two numbers by without using recursion.
'''
# head_values = [12,15]

# def find_hcf(num1, num2):
#     while num2:
#         num1, num2 = num2, num1 % num2  # 15 , 12  # 12 3 # 3 0
#         print('num1',num1)
#         print ('num2 =================',num2)
#     return num1

# print (find_hcf(12,15))

#! 2- series of characters

'''
Consider a string, S, that is a series of characters,
each followed by its frequency as an integer. The string
is not compressed correctly, so there may be multiple occurrences
 of the same character. A properly compressed string will consist
 of one instance of each character in alphabetical order followed
 by the total count of that character within the string.
'''

'''
we need to take the letters and create a list of them
then we need to take the numbers by skipping one taking even indexes
we need to have a set so we don't have repetitions or we need to have a counter and then we just return the letter but the counts

'''

# def letters(s):
#     arr = list(enumerate(s))
#     print (arr)
#     st = defaultdict()
#     for index, item in arr:
#         if item.isalpha() and item not in st:
#             st[item] = s[index+1]
#         elif item.isalpha() and item in st:
#             st[item] += s[index+1]

#     print (st)


# s= "a3b5c2a2"

# letters(s)

#! 3- get Minimum Moves
'''
shopkeeper sells n items where the price of the th item is price[i].
To maintain balance, the shopkeeper wishes to adjust the price of
items such that the median of prices is exactly k.
 In one move, the shopkeeper can increase or decrease the price of any item by 1,
   and the shopkeeper can perform this move any number of times.
   Find the minimum number of moves in which the median of prices becomes exactly k.
   ExampleConsider
   n = 5,
   Price = [4, 2, 1, 4, 7]
   and k = 3.
   Note: The index of the median of an array of m sorted elements, where mis odd, is (m+1)/2.
   For example, [2, 5, 4, 1, 1, 1, 6] sorted is [1, 1, 1, 2, 4, 5, 6].
   Its length is 7 so the median is at index (7 + 1)/2 = 4 using 1-based indexing.
 The median is 2.GithubDecrease price[0] by 1, the resulting array is [3, 2, 1, 4, 7];
 on sorting, this becomes [1, 2, 3, 4, 7], whose median equals k = 3.
 Thus, in one move, the median becomes 3 and the answer is 1.
 Function DescriptionComplete the function getMinimum Moves in the editor below.
 getMinimum Moves has the following parameters:int price[n]: the prices of
 itemsint k: the required medianReturnslong_int. the minimum number of moves
 to make the median of the array exactly kConstraintsTyping• 10 105●1 = price[i], k = 10⁹
 It is guaranteed that nis odd

'''
def getMinimumMoves(price, k):
    price.sort()  # Step 1: Sort the array
    n = len(price)
    median_index = (n + 1) // 2 - 1  # Step 2: Find the index of the median

    moves = 0
    median_price = price[median_index]

    if median_price < k:  # If current median is less than k
        for i in range(median_index, n):
            if price[i] < k:
                moves += k - price[i]
    elif median_price > k:  # If current median is greater than k
        for i in range(median_index, -1, -1):
            if price[i] > k:
                moves += price[i] - k

    return moves

# Test example
price = [4, 2, 1, 4, 7]
# price = [3, 3, 6, 3, 9]
k = 3
# k = 2
print(getMinimumMoves(price, k))  # Output: 1
