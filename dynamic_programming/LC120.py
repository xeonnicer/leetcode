from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        depth = len(triangle)
        # define dp[i][j] = the min path sum of triangle[i][j]
        # dp = [0 for _ in range(depth)]

        dp = [[0 for j in range(len(triangle[-1]))] for i in triangle]
        dp[0][0] = triangle[0][0]

        for i in range(1, depth):
            # three situation
            # 1: first cell
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            # 2: cell between first -> last
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            # 3: last cell
            dp[i][i] = dp[i-1][i-1] +  triangle[i][i]
        # for i in dp:
        #     print(i)
        return min(dp[-1])
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
ans = Solution().minimumTotal(triangle)
print(ans)
