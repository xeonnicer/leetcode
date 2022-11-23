"""
初始时有n 个灯泡处于关闭状态。第一轮，你将会打开所有灯泡。接下来的第二轮，你将会每两个灯泡关闭第二个。

第三轮，你每三个灯泡就切换第三个灯泡的开关（即，打开变关闭，关闭变打开）。第 i 轮，你每 i 个灯泡就切换第 i 个灯泡的开关。直到第 n 轮，你只需要切换最后一个灯泡的开关。

找出并返回 n轮后有多少个亮着的灯泡。


"""
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


# class Solution:
#     def bulbSwitch(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return n
#         dp = [True for i in range(n)]
#         for i in range(2, n + 1):
#             if i == n:
#                 dp[-1] = not dp[-1]
#                 break
#             for j in range(n):
#                 dp[j] = not dp[j] if (j + 1) % i == 0 else dp[j]
#
#         print(dp)
#         return sum(dp)


n = 4
ans = Solution().bulbSwitch(n)
print(ans)
