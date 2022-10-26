"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = int(a, 2) + int(b, 2)
        print(ans)
        return bin(ans)[2:]


a = '1010'
b = '1011'
ans = Solution().addBinary(a, b)
print(ans)
