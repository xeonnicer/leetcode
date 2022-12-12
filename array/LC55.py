"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):

            # print(i, reach)
            if reach < i:
                return False
            reach = max(reach, nums[i] + i)
        return True


# nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
nums = [2, 0, 0]
ans = Solution().canJump(nums)

print(ans)
