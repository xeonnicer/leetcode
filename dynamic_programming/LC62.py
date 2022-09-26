class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n ==0:
            return 0
        # define dp[i] = sum(available path [i - j])
        dp = [[0 for _n in range(n)] for _m in range(m)]
        dp[0][0] = 1

        for _m in range(m):
            for _n in range(n):
                if _m == 0 and _n == 0:
                    continue
                # three condition
                if _n > 0:
                    dp[_m][_n] += dp[_m][_n - 1]
                if _m > 0:
                    dp[_m][_n] += dp[_m - 1][_n]
        # for i in dp:
        #     print(i)
        return dp[m-1][n-1]
ans = Solution().uniquePaths(3, 7)
# print(ans)

