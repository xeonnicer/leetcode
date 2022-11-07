"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []

        def backTracing(n, k, index):
            if len(path) == k:
                # if len(set(path)) < len(path):
                #     return
                result.append(path.copy())
                return
            for i in range(len(n)):
                path.append(n[i])
                _tmp = n.copy()
                _tmp.pop(i)
                backTracing(_tmp, k, i + 1)
                path.pop()

        backTracing(nums, len(nums), 0)
        return result


nums = nums = [1, 2, 3]
ans = Solution().permute(nums)
print(ans)
