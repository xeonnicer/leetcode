"""给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []

        def backtracing(n, k, used: List[int]):
            if len(path) == k:
                result.append(path.copy())
                return
            for i in range(len(n)):
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracing(n, k, used)
                path.pop()
                used[i] = False

        used = [False for i in nums]
        nums.sort()
        backtracing(nums, len(nums), used)
        return result


nums = [1, 1, 2]
ans = Solution().permuteUnique(nums)
print(ans)
