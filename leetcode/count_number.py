"""
1523. 在区间范围内统计奇数数目
给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。
"""
import math


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = high - low + 1
        if count % 2 == 0:
            return int(count / 2)
        else:
            if low % 2 == 0:
                return int(math.floor(count / 2))
            else:
                return int(math.ceil(count / 2))


sln = Solution()
sln.countOdds(1, 5)
