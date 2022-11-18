from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n + 1)
        m = len(primes)
        pointers = [0] * m
        nums = [1] * m

        for i in range(1, n + 1):
            min_num = min(nums)
            dp[i] = min_num
            for j in range(m):
                if nums[j] == min_num:
                    pointers[j] += 1
                    nums[j] = dp[pointers[j]] * primes[j]

        return dp[n]


n = 12
primes = [2, 7, 13, 19]
Solution().nthSuperUglyNumber(n, primes)
