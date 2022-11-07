"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.path = list()
        self.result = list()
        self.back_tracing(n, k, 1)
        return self.result.copy()

    def back_tracing(self, n, k, start_idx):

        if len(self.path) == k:
            self.result.append(self.path.copy())

            return
        for i in range(start_idx, n + 1):
            self.path.append(i)
            self.back_tracing(n, k, i + 1)
            self.path.pop()


n = 4
k = 2
ans = Solution().combine(n, k)
print(ans)
