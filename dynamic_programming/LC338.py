"""
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for i in range(n+1)]
        for i in range(1, n + 1):

            if i % 2 == 0:
                print('get in oushu')
                print(i)
                dp[i] = dp[int(i / 2)]
            else:
                print('get in jishu')
                print(i)
                dp[i] = dp[i - 1] + 1
        return dp


sln = Solution()
res = sln.countBits(2)
print(res)
# a = []
