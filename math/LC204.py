"""
给定整数 n ，返回 所有小于非负整数 n 的质数的数量
"""
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [1 for i in range(n)]
        count = 0
        for i in range(2, n):
            if prime[i]:
                count += 1
                for j in range(i ** 2, n, i):
                    prime[j] = 0
        return count


n = 1
ans = Solution().countPrimes(n)
print(ans)