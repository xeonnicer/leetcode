"""
f(x) = {
f(0) = 0 , x = 0
f(1) = nums[0], x = 1
f(x) = max( dp[j] + 1, dp[i] ) if nums[i] > nums[j] ,x > 1

}
"""
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if not length:
            return 0
        if length == 1:
            return 1
        dp = [1 for i in range(length)]
        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
nums = [1,3,6,7,9,4,10,5,6]
ans = Solution().lengthOfLIS(nums)
print(ans)
