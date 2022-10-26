class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        row = len(s) + 1
        col = len(t) + 1
        dp = [ [False for j in range(col)] for i in range(row)]

        for i in range(col):
           dp[0][i] = True
        for r in range(1,row):
            for c in range(1,col):
                # print(s[r-1], t[c-1])
                if s[r-1] == t[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                elif dp[r][c-1] == True:
                    dp[r][c] = True
                elif dp[r][c-1] == False:
                    dp[r][c] = False
        for i in dp:
            print(i)
        return dp[row-1][col-1]

ans = Solution().isSubsequence('ACCA','AABCACCA')
print(ans)