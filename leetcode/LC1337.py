"""
给你一个大小为m* n的矩阵mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。

请你返回矩阵中战斗力最弱的k行的索引，按从最弱到最强排序。

如果第i行的军人数量少于第j行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。

军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前
"""
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        _map = {}
        for index, i in enumerate(mat):
            _map.update({index: sum(i)})
        _tmp = sorted(_map.items(), key=lambda x: x[1])
        return [i[0] for i in _tmp][:k]


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3

ans = Solution().kWeakestRows(mat, k)
print(ans)
