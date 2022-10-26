from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # define dp[i] = last i characters  in wordDict
        length = len(s)
        dp = [False for i in range(length + 1)]
        dp[0] = True
        for i in range(length):
            for j in range(i + 1, length + 1):
                if (dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
                    

        # print(dp)
        return dp[length]


s = "aaaaaaa"
wordDict = ["aaaa", "aaa"]
ans = Solution().wordBreak(s, wordDict)
print(ans)
