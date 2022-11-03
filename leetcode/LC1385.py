"""
给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。

「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。


"""
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = sorted(arr2)
        count = 0
        for i in arr1:
            if self.binary_search(i, d, arr2):
                continue
            else:
                count += 1
        return count

    def binary_search(self, x, d, arr) -> bool:
        l = 0
        r = len(arr) - 1
        small = x - d
        big = x + d
        while l <= r:
            mid = l + (r - l) // 2
            if small <= arr[mid] <= big:
                print(arr[mid])
                return True
            elif arr[mid] > big:
                l = mid + 1
            elif arr[mid] < small:
                r = mid - 1
        return False


# arr1 = [1, 4, 2, 3]
# arr2 = [-4, -3, 6, 10, 20, 30]
# d = 3
# arr1 = [2, 1, 100, 3]
# arr2 = [-5, -2, 10, -3, 7]
# d = 6

# arr1 = [4, 5, 8]
# arr2 = [10, 9, 1, 8]
# d = 2

arr1 = [-3, 10, 2, 8, 0, 10]
arr2 = [-9, -1, -4, -9, -8]
d = 9
ans = Solution().findTheDistanceValue(arr1, arr2, d)
print(ans)
import bisect
bisect.bisect_left(arr2, x)
