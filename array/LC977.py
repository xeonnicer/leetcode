"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []

        length = len(nums)
        i = 0
        j = length - 1
        while i <= j:
            if nums[i] ** 2 < nums[j] ** 2:
                result.insert(0, nums[j] ** 2)
                j -= 1

            else:
                result.insert(0, nums[i] ** 2)
                i += 1
        return result


nums = nums = [-7,-3,2,3,11]
ans = Solution().sortedSquares(nums)
print(ans)
