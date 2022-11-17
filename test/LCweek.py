# from typing import List
# 
# 
# class Solution:
#     def convertTemperature(self, celsius: float) -> List[float]:
#         return [celsius + 273.15, celsius * 1.80 + 32]
# 
# 
# celsius = 36.50
# ans = Solution().convertTemperature(celsius)
# print(ans)

# 6234. 最小公倍数为 K 的子数组数目
from typing import List

# class Solution:
#     def subarrayLCM(self, nums: List[int], k: int) -> int:
#         test = [2, 3, 5, 7, 11, 13, 17, 19]
#         public_ = [i for i in nums if k / i in test and i != 1 or k == i]
#         public_.sort()
#         print(public_)
#         path = []
#         result = []
#         length = len(public_)
#
#         def backTracing(n, k, index):
#
#
# nums = [3, 6, 2, 7, 1]
# k = 6
#
# ans = Solution().subarrayLCM(nums, k)

count = 0

import sys


# 6235. 逐层排序二叉树所需的最少操作数目
# def insertionSort(arr):
#     global count
#     for i in range(1, len(arr)):
#
#         key = arr[i]
#
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#         count += 1
def my_sort(nums: List, count=0):
    count = 0
    arr_copy = nums.copy()
    arr_sorted = arr_copy.sort()
    for i in range(len(nums) - 1):
        if arr_sorted == nums:
            break
        index = nums.index(min(nums[i + 1:]))
        if nums[index] < nums[i]:
            nums[index], nums[i] = nums[i], nums[index]
            count += 1

    return nums


# count = 0
# arr = [4, 3]
#
# my_sort(arr, count)

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        pass
