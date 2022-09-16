class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        row = len(s) + 2
        col = len(t) + 2
        dp = [ [False for j in range(col)] for i in range(row)]
        for i in dp[1]:
            i = True
        for i in range(2, row):
            dp[1][i] = False
        for r in range(1,row):
            for c in range(1,col):
                if dp[r]:
                    pass

ans = Solution().isSubsequence('asdf','asdfafasdfadfa')