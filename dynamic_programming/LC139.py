from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # define dp[i] = last i characters  in wordDict
        length = len(s)
        dp = [False for i in range(length + 1)]
        dp[0] = 0