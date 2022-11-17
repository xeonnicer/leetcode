"""
给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b

"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]
        # elif len(arr) <= k:
        #     return arr
        index = self.binary_search(arr, x)
        print('index', index)
        if arr[index] == x:
            l = r = index
            count = 1
        else:
            l = index
            r = index + 1
            count = 2
        if k == 1:
            return [arr[l]] if abs(arr[l] - x) < abs(arr[r] - x) else [arr[r]]
        for _ in range(k):
            if l < 0:
                r += 1
            elif r >= len(arr) or x - arr[l] <= arr[r] - x:
                l -= 1
            else:
                r += 1

        # print('l, r:', l, r)
        return arr[l:r]

    def binary_search(self, arr: List, target):
        # find the element which nearest target
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(mid)
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return r


from bisect import bisect_left


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect_left(arr, x)
        left = right - 1
        print(left, right)
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) or x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1: right]


arr = [1, 2, 3, 4, 5]
k = 4
x = 3

# arr = [1, 2, 3, 4, 5]
# k = 4
# x = -1

arr = [1, 1, 1, 10, 10, 10]
k = 1
x = 9
arr = [-2, -1, 1, 2, 3, 4, 5]
k = 7
x = 3
ans = Solution().findClosestElements(arr, k, x)
print(ans)
