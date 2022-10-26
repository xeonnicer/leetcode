from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # define dp[i] = max sum of  the first i nums
        length = len(nums)
        if not nums:
            return 0
        dp_max = [-9999 for i in range(length)]
        dp_max[0] = nums[0]
        dp_min = [9999 for i in range(length)]
        dp_min[0] = nums[0]
        max_num = nums[0]
        for i in range(1, length):
            dp_max[i] = max(dp_min[i - 1] * nums[i], nums[i], dp_max[i - 1] * nums[i])
            dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
            max_num = max(max_num, dp_max[i])
        # print(dp_max)
        # print(dp_min)
        return max_num


nums = [2, 3, -2, 4]
ans = Solution().maxProduct(nums)
print(ans)
