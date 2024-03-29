from typing import List
from typing import Optional, List
from collections import defaultdict, Counter

#! 1- bubble sort
# def bubble_sort(arr):
#     n = len(arr)

#     # Traverse through all array elements
#     for index in range(n):
#         print('index====================', index)
#         # print('n' , n)
#         # Last i elements are already in place, so we don't need to check them
#         for j in range(0, n-index-1):
#             # print (n-index-1)
#             print ('arr' , arr)
#             print ('index',arr[index])
#             print ('J',j)
#             print ('arr[J]',arr[j])
#             print ('J+1',arr[j+1])
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# # Example usage:
# # my_list = [64, 34, 25, 12, 22, 11, 90]
# my_list = [64, 34, 25, 12, 22, 90, 11]
# # my_list = [64, 34, 25, 12, 90, 22, 11]
# bubble_sort(my_list)

# print("Sorted array:", my_list)

#! 2- Another bubble sort

# def bubble_sort2( nums):

#     for i in range(len(nums)):
#         for j in range (len(nums)-1):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j]= nums[j+1]
#                 nums[j+1] = temp
#     return nums
# # Example usage:
# # my_list = [64, 34, 25, 12, 22, 11, 90]
# my_list = [64, 34, 25, 12, 22, 90, 11]
# # my_list = [64, 34, 25, 12, 90, 22, 11]
# bubble_sort2(my_list)

# print("Sorted array:", my_list)


#! 3-binary search # don't use this use the one in 704

# def binary_search(arr, l, r, x):
#     if r >= l:
#         mid = l + (r - l) // 2
#         '''
#         you can also use mid = (l + r) // 2 but the first one is preferred
#         helps prevent integer overflow because it reduces the risk of exceeding
#           the maximum representable integer value. If l and r are very large,
#             their sum might exceed the maximum integer value that the programming
#               language can handle, potentially leading to unexpected behavior.
#         '''

#         if arr[mid] == x:
#             return mid

#         elif arr[mid] > x:
#             return binary_search(arr, l, mid - 1, x)

#         else:
#             return binary_search(arr, mid + 1, r, x)

#     return -1

# # Example array (must be sorted for binary search)
# sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Element to search for
# target_element = 7

# # Initial search range (l and r are the indices)
# left_index = 0
# right_index = len(sorted_array) - 1

# # Perform binary search
# result = binary_search(sorted_array, left_index, right_index, target_element)

# # Check the result
# if result != -1:
#     print(f"Element {target_element} found at index {result}.")
# else:
#     print(f"Element {target_element} not found in the array.")


#! 4-binary search another approach
# def binary_search2(nums, l, r, target):
#     if r >= l:

#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if target < nums[mid]:
#                 r = mid - 1
#             elif target > nums[mid]:
#                 l = mid + 1
#             else:
#                 print(mid)
#                 break
#     return mid

# # Example array (must be sorted for binary search)
# sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Element to search for
# target_element = 7

# # Initial search range (l and r are the indices)
# left_index = 0
# right_index = len(sorted_array) - 1

# # Perform binary search
# result = binary_search2(sorted_array, left_index, right_index, target_element)

# # Check the result
# if result != -1:
#     print(f"Element {target_element} found at index {result}.")
# else:
#     print(f"Element {target_element} not found in the array.")


#! 5- 75. Sort Colors (Algo Academy) (medium) (algorithm/Tech: "Dutch National Flag" algorithm. (it is not bucket sort) )

'''
75. Sort Colors
Medium
Topics
Companies
Hint
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2. #! when we are limited to few options is a good indicator to use bucket sort

'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counts = [0] *3
        # for n in nums:
        #     counts[n] += 1
        #     # print(counts)
        # i = 0
        # #! Outer loop: Iterate through each color (0, 1, 2)
        # for n in range(len(counts)):
        #     print ('length count>>>>>>', len(counts))
        #     print ('n ++++', n)
        #     #! Inner loop: Iterate through the count of each color
        #     for c in range(counts[n]):
        #         print ('counts[n]====', range(counts[n]))
        #          #! Assign the current color to the current index in the original list nums
        #         nums[i] = n
        #         print ('nums **********************************' , nums)
        #         print ('nums[i]' ,nums[i])
        #         #! Increment the index
        #         i+=1
        #         print ( 'iiiiii', i)
        # without the prints
        # counts = [0,0,0]
        # for n in nums:
        #     counts[n] +=1
        # i = 0
        # for n in range(len(counts)):
        #     for c in range(counts[n]):
        #         nums[i]= n
        #         i +=1



# nums = [2,0,2,1,1,0]
# solution = Solution()
# output = solution.sortColors(nums)
# print(nums)


#! - example of bucket sort (with insertion sort) (it uses other sorting methods to sort )

# Python3 program to sort an array
# using bucket sort


# def insertionSort(b):
# 	for i in range(1, len(b)):
# 		up = b[i]
# 		j = i - 1
# 		while j >= 0 and b[j] > up:
# 			b[j + 1] = b[j]
# 			j -= 1
# 		b[j + 1] = up
# 	return b


# def bucketSort(x):
# 	arr = []
# 	slot_num = 10 # 10 means 10 slots, each
# 	# slot's size is 0.1
# 	for i in range(slot_num):
# 		arr.append([])

# 	# Put array elements in different buckets
# 	for j in x:
# 		index_b = int(slot_num * j)
# 		arr[index_b].append(j)

# 	# Sort individual buckets
# 	for i in range(slot_num):
# 		arr[i] = insertionSort(arr[i])

# 	# concatenate the result
# 	k = 0
# 	for i in range(slot_num):
# 		for j in range(len(arr[i])):
# 			x[k] = arr[i][j]
# 			k += 1
# 	return x


# # Driver Code
# x = [0.897, 0.565, 0.656,
# 	0.1234, 0.665, 0.3434]
# print("Sorted Array is")
# print(bucketSort(x))


#! 5- 912. Sort an Array (Algo Academy) (medium) (algorithm/Tech: merge sort)

'''
912. Sort an Array
Medium
Topics
Companies Google Apple Microsoft
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.


Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104

'''
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         if len(nums) < 2: return nums

#         mid = len(nums)//2
#         left = self.sortArray(nums [0:mid])
#         right = self.sortArray(nums[mid::])

#         return self.merge(left,right)


#     def merge(self,left,right):
#         merged = []
#         while len(left) and len(right):
#             if left[0] < right[0]:
#                 merged.append(left.pop(0))
#             else:
#                 merged.append(right.pop(0))

#         return merged + left + right

# #another GPT solution

#     # class Solution:
#     # def sortArray(self, nums: List[int]) -> List[int]:
#     #     if len(nums) < 2:
#     #         return nums

#     #     mid = len(nums) // 2
#     #     left = self.sortArray(nums[:mid])
#     #     right = self.sortArray(nums[mid:])

#     #     return self.merge(left, right)

#     # def merge(self, left: List[int], right: List[int]) -> List[int]:
#     #     merged = []
#     #     i = j = 0

#     #     while i < len(left) and j < len(right):
#     #         if left[i] < right[j]:
#     #             merged.append(left[i])
#     #             i += 1
#     #         else:
#     #             merged.append(right[j])
#     #             j += 1

#     #     merged.extend(left[i:])
#     #     merged.extend(right[j:])

#     #     return merged

# nums = [5,1,1,2,0,0]

# # output = Solution.sortArray(nums)
# output = Solution().sortArray(nums)
# print(output)


#! 6- 912. Sort Characters By Frequency (Algo Academy) (medium) (algorithm/Tech: bucket sort) (time complexity O(n) n is length of string)

'''
451. Sort Characters By Frequency
Medium
Topics
Companies
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.



Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.


'''
# class Solution:
#     def frequencySort(self, s: str) -> str:

#         n = len(s)
#         # print('n' , n)
#         c = Counter(s)
#         # print('c-items', c.items())

#         bucket = [[] for _ in range(n+1)] #! b/c below the reverse range starts from n which is = 4
#         # print ('bucket', bucket )

#         for char, freq in c.items(): # we must items to iterate otherwise it will only iterate over keys if just used (c)
#             bucket[freq].append(char) # we go to the list in the list with bucker[freq]
#             # print ("bucket", bucket)

#             # print ("bucket[1]", bucket[1])
#                 # print ("teezzzzi", teezi)
#             # print('bucket keys+++++++++++++',bucket.keys())


#         res = ''

#         for freq in range(n,0,-1):
#             print ('freq' , freq)
#             for char in bucket[freq]:
#                 # print('CHAR', char)
#                 # print( 'bucket[freq]================'  ,bucket[freq])
#                 res += freq*char
#                 # print ('freq*char',freq*char)
#         return res

# # s ="Abcddeee" # eeeddAbc
# # s = "Aabb" # bbAa
# s = "tree" # eetr
# output = Solution().frequencySort(s)
# print(output)

#! 7- 704. Binary Search (Algo Academy) (easy) (algorithm/Tech: iterative binary search) (time complexity O(log(n)) n is length of array)


'''
704. Binary Search
Easy
Topics
Companies
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.


'''
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0 , len(nums)-1

#         while left <= right:
#             mid = left + (right-left)//2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid]> target:
#                 right = mid-1
#             else:
#                 left = mid + 1
#         return -1




# nums = [-1,0,3,5,9,12]

# target = 9

# output = Solution().search(nums,target)
# print(output)


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         def recurse(left, right):
#             if left >=right:
#                 return right if nums[right] == target else -1
#             mid = left + (right- left)//2

#             if nums[mid] == target:
#                 return mid
#             elif target < nums[mid]:
#                 return recurse(left, mid-1)
#             else:
#                 return recurse(mid+1, right)

#         return recurse(0, len(nums)-1)





# nums = [-1,0,3,5,9,12]

# target = 9

# output = Solution().search(nums,target)
# print(output)


#! 7- 374. Guess Number Higher or Lower (Algo Academy) (easy) (algorithm/Tech: iterative binary search) (time complexity O(log(n)) n is length of array)

'''
374. Guess Number Higher or Lower
Easy
Topics
Companies
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.



Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1


Constraints:

1 <= n <= 231 - 1
1 <= pick <= n

'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int: pass

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0 , n

        while left <= right:
            mid = left + (right-left)//2
            if guess(mid) == -1:
                right = mid -1
            elif guess(mid) == 1:
                left = mid +1
            else:
                return mid




n = 10 # you need to access the api for this to get a response 
pick = 6

output = Solution().guessNumber(n)
print(output)
