"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for index, i in enumerate(nums):
            j = target - i
            index_j = cache.get(j)
            if index_j != None and index_j != index:
                return [index, index_j]
            cache.update({i: index})


nums = [3, 3]
target = 6
sln = Solution()
res = sln.twoSum(nums, target)
print(res)
