from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m > 0:
            n = len(obstacleGrid[0])
        else:
            n = 0
        if m == 0 and n == 0:
            return 0
        # define dp[i] = sum(available path [i - j])
        dp = [[0 for _n in range(n)] for _m in range(m)]
        # print(m, n)
        if m + n <= 1:
            return 0
        if m + n > 0:
            if obstacleGrid[0][0] == 1:
                return 0
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        dp[0][0] = 1

        for _m in range(m):
            for _n in range(n):
                if obstacleGrid[_m][_n] == 1:
                    continue
                if _m == 0 and _n == 0:
                    continue
                # three condition
                if _n > 0:
                    dp[_m][_n] += dp[_m][_n - 1]
                if _m > 0:
                    dp[_m][_n] += dp[_m - 1][_n]
        # for i in dp:
        #     print(i)
        return dp[m - 1][n - 1]

obstacleGrid = [[]]

ans = Solution().uniquePathsWithObstacles(obstacleGrid)
print(ans)