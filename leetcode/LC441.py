"""
你总共有n枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。

给你一个数字n ，计算并返回可形成 完整阶梯行 的总行数。

。
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n

        while l < r:
            mid = (l+r+1) // 2
            total = mid * (mid + 1) // 2
            # print('mid: ',mid)
            # print('total: ', total)
            if total <= n:
                l = mid
            elif n < total:
                r = mid -1
            # else:
            #     return l

        return l
n = 100
ans = Solution().arrangeCoins(n)
print(ans)