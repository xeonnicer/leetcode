class Solution:
    def numDecodings(self, s: str) -> int:

        # define dp[i] = max solution of the first i of "s"
        length = len(s)
        dp = [0 for _ in range(length)]
        if not s or s.startswith('0'):
            return 0
        dp[0] = 1
        # print(dp[0])
        for i in range(1, length):
            if int(s[i - 1:i+1]) <= 26 and s[i - 1] != '0':
                # print(s[i - 1:i+1])
                # print(i)
                dp[i] = dp[i - 1] + 1
            elif int(s[i - 1:i+1]) > 26 and s[i] == '0':
                return 0
            else:
                dp[i] = dp[i-1]
        return dp[length-1]

s = "10"
ans = Solution().numDecodings(s)
print(ans)