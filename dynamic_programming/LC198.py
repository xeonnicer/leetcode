"""
f(x) = {
    nums[0], x = 1
    max(nums[0], nums[1]), x = 2
    max(f(x-2) + nums[x], nums[x-1]  ), x>2
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if not length:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        dp = [0 for i in range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):

            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        print(dp)
        return dp[length - 1]

nums = [1,2,3,1]
ans = Solution().rob(nums)
print(ans)