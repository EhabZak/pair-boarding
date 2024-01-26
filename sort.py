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


#! 3-binary search

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
#         mid = l + (r - l) // 2
#         '''
#         you can also use mid = (l + r) // 2 but the first one is preferred
#         helps prevent integer overflow because it reduces the risk of exceeding
#           the maximum representable integer value. If l and r are very large,
#             their sum might exceed the maximum integer value that the programming
#               language can handle, potentially leading to unexpected behavior.
#         '''
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             m = (l + r) // 2
#             if target < nums[m]:
#                 r = m - 1
#             elif target > nums[m]:
#                 l = m + 1
#             else:
#                 print(m)
#                 break
#     return m

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
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums

        mid = len(nums)//2
        left = self.sortArray(nums [0:mid])
        right = self.sortArray(nums[mid::])

        return self.merge(left,right)


    def merge(self,left,right):
        merged = []
        while len(left) and len(right):
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))

        return merged + left + right

#another GPT solution

    # class Solution:
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     if len(nums) < 2:
    #         return nums

    #     mid = len(nums) // 2
    #     left = self.sortArray(nums[:mid])
    #     right = self.sortArray(nums[mid:])

    #     return self.merge(left, right)

    # def merge(self, left: List[int], right: List[int]) -> List[int]:
    #     merged = []
    #     i = j = 0

    #     while i < len(left) and j < len(right):
    #         if left[i] < right[j]:
    #             merged.append(left[i])
    #             i += 1
    #         else:
    #             merged.append(right[j])
    #             j += 1

    #     merged.extend(left[i:])
    #     merged.extend(right[j:])

    #     return merged

nums = [5,1,1,2,0,0]

# output = Solution.sortArray(nums)
output = Solution().sortArray(nums)
print(output)
