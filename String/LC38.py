class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return '10'
        dp = ['0'] * (n + 1)
        dp[1] = '1'
        for i in range(2, n + 1):
            _tmp = []  # [(1, n=3), (2, n=2), (1, n=1)]
            for index, s in enumerate(dp[i - 1]):
                if index == 0 or dp[i - 1][index] != dp[i - 1][index - 1]:
                    _tmp.append([s, 1])
                else:
                    _tmp[-1][1] += 1
            # print(_tmp)
            res = []
            for j in _tmp:
                res.extend([str(j[1]), j[0]])
            # print(res)
            # print(i)
            dp[i] = ''.join(res)
        # for i in dp:
        #     print(i)

        return dp[n]


n = 5
ans = Solution().countAndSay(n)
print(ans)
