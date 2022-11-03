"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        # find left border
        while l <= r:

            mid = l + r >> 1
            # print("l:", l)
            # print("r:", r)
            # print("mid:", mid)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        # print("finally left:", l)
        l_tmp = l
        if l >= len(nums):
            return [-1, -1]
        if nums[l_tmp] != target:
            return [-1, -1]
        # find right border
        r = len(nums) - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [l_tmp, r]


nums = [2, 2]
target = 3
ans = Solution().searchRange(nums, target)
print(ans)
