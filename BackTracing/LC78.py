"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []

        def backTracing(n, k, index):
            if len(path) > k:
                return
            else:
                result.append(path.copy())
            for i in range(index, len(n)):
                path.append(n[i])
                # _tmp = n.copy()
                # _tmp.pop(i)
                backTracing(n, k, i + 1)
                path.pop()

        backTracing(nums, len(nums), 0)
        return result


nums = [1, 2, 3]
ans = Solution().subsets(nums)
print(ans)
