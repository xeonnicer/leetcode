from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        dp = [[0 for j in range(numRows)] for i in range(numRows)]
        for i in range(numRows):
            for j in range(numRows):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
                dp[i][i] = 1
        for i in range(numRows):
            for j in range(numRows):
                if dp[i][j] == 0 and j < i:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        ans = []
        for i in dp:
            _tmp = []
            for j in i:

                if j != 0:
                    _tmp.append(j)
            ans.append(_tmp)
        return ans


ans = Solution().generate(5)
print(ans)
