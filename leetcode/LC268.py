"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        expected_sum = length * (length + 1) // 2
        real_sum = sum(nums)
        return int(expected_sum - real_sum)


nums = [3, 0, 1]
ans = Solution().missingNumber(nums)
print(ans)
