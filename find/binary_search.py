"""
704. 二分查找
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = self.binary_search(nums, 0, len(nums) - 1, target)
        return res

    def binary_search(self, nums, low, high, target):
        mid = math.floor((high - low) / 2 + low)
        if nums[mid] == target:
            return mid
        if low >= high or high <= low:
            return -1
        elif nums[mid] < target:
            return self.binary_search(nums, mid + 1, high, target)
        elif nums[mid] > target:
            return self.binary_search(nums, low, mid - 1, target)


sln = Solution()
target = 9
nums = [-1, 0, 3, 5, 9, 12]
print(sln.search(nums, target))
