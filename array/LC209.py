"""
给定一个含有n个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 10 ** 6
        i = 0
        sum = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                length = j - i + 1
                result = min(result, length)
                sum -= nums[i]
                i += 1
        if result == 10 ** 6:
            return 0
        return result


target = 4
nums = [1, 4, 4]
ans = Solution().minSubArrayLen(target, nums)
print(ans)
