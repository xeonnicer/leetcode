"""
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # length = len(nums)
        # j = 0
        # mv = nums[j]
        # for i in range(length):
        #     new_idx = (j + k) % length
        #     print(j)
        #     print(k)
        #     print(new_idx)
        #     _copy = nums[new_idx]
        #     nums[new_idx] = mv
        #     mv = _copy
        #     j = new_idx
        length = len(nums)
        k %= length
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]



# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
nums = [-1, -100, 3, 99]
k = 2
Solution().rotate(nums, k)
print(nums)
