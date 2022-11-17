"""
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

"""


class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(1, n):
            if i ** 2 <= n:
                nums.append(i ** 2)
        # 在前i个数中任选拼成j的使用最少的数字
        _max = 10 ** 5
        dp = [[_max for i in range(n + 1)] for i in range(len(nums))]
        for i in range(n + 1):
            dp[0][i] = nums[0] * i
        for i in range(len(nums)):
            dp[i][0] = 0
        for j in range(1, n + 1):
            for i in range(1, len(nums)):
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - nums[i]] + 1)
        # for i in dp:
        #     print(i)
        return dp[-1][-1]


n = 12
n = 16
n = 16
ans = Solution().numSquares(n)
print(ans)
