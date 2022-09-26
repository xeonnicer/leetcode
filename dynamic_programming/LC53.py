from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        # define dp[i] = The last element is the sum of the largest subnumbers of i
        #     print(i)
        dp = [0 for i in range(length)]
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, length):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
            max_sum = max(dp[i], max_sum)
        return max_sum
test_case = [-2,1,-3,4,-1,2,1,-5,4]
ans = Solution().maxSubArray(test_case)
print(ans)