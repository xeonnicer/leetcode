from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l = 0
        r = length
        while l < r:
            mid = (r - l) // 2 + l
            print(mid)
            if nums[mid] == target:
                # print('get in == ')
                return mid
            elif nums[mid] < target:
                # print('get in < ')
                l = mid + 1
            elif nums[mid] > target:
                # print('get in > ')
                r = mid

        return l


nums = [1, 3, 5, 6]
target = 9
ans = Solution().searchInsert(nums, target)
print('---------')
print(ans)


