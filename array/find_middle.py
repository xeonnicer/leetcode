from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums) == nums[0]:
            return 0
        for index in range(1, len(nums)):

            if sum(nums[:index]) == sum(nums[index + 1:]):
                return index
        return -1


a = [1, 2, 3]
ans = Solution().pivotIndex(a)
print(ans)
