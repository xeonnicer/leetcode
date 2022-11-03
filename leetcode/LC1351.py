"""
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 请你统计并返回 grid 中 负数 的数目。

"""
from typing import List


# binary search ,search the biggest number which smaller than 0


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        count = 0
        for arr in grid:
            if arr[-1] >= 0:
                continue
            index = self.binary_search(arr)
            # print('-------------')
            # print(arr)
            # print(index)
            count += m - index
        return count

    def binary_search(self, arr: List):
        l = 0
        r = len(arr) - 1
        while l < r and arr[l] >= 0:
            mid = (l + r) // 2
            if arr[mid] >= 0:
                l = mid + 1
            else:
                r = mid

        return l


grid = [[3, 2], [1, 0]]
grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
# grid = [[3, -1, -3, -3, -3], [2, -2, -3, -3, -3], [1, -2, -3, -3, -3], [0, -3, -3, -3, -3]]

ans = Solution().countNegatives(grid)
print(ans)
# index = Solution().binary_search(grid[0])
# print(index)
