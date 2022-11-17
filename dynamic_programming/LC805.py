"""
给定你一个整数数组nums

我们要将nums数组中的每个元素移动到A数组 或者B数组中，使得A数组和B数组不为空，并且average(A) == average(B)。

如果可以完成则返回true， 否则返回 false。

注意：对于数组arr, average(arr)是arr的所有元素的和除以arr长度。

"""
from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        ave = sum(nums) / len(nums)
        target = (len(nums) + 1) // 2 * ave
        if target != int(target):
            return False
        print(target)
        target = int((len(nums) + 1) // 2 * ave)
        dp = [[0 for j in range(target + 1)] for i in range(len(nums))]
        for j in range(target + 1):
            dp[0][j] = nums[0]

        # for i in range(len(nums)):
        #     dp[i][0] = 0
        for i in range(1, len(nums)):
            for j in range( target + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], + dp[i - 1][j - nums[i]] + nums[i])
        for x in dp:
            print(x)
        if dp[i][j] == target:
            return True
        else:
            return False


nums = [1, 2, 3, 4, 5, 6, 7, 8]
# nums = [1, 3]
# nums = [6, 8, 18, 3, 1]
# nums = [18, 10, 5, 3]

ans = Solution().splitArraySameAverage(nums)
print(ans)
