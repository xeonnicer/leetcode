class Solution:
    def longestPalindrome(self, s: str) -> str:
        length  = len(s)
        if length <= 1:
            return s
        max_len = 1
        begin = 0
        dp = [[True if i == j else False for j in range(length)] for i in range(length)]
        for j in range(1, length):
            for i in range(length):
                if i >=j:
                    continue

                if s[i] != s[j]:
                    dp[i][j] = False
                elif j - i +1 < 3:
                    dp[i][j] = True
                else:
                    dp[i][j]  = (s[i] == s[j] and dp[i+1][j-1]) or False


                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        # for i in dp:
        #     print(i)
        return s[begin:begin + max_len]
ans = Solution().longestPalindrome('cbbd')
print(ans)