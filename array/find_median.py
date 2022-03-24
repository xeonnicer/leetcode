"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        # calcul index
        if (m + n) % 2 == 0:
            index = [(m + n) / 2 - 1, (m + n) / 2]
        else:
            index = [math.floor((m + n) / 2)]
        print(index)
        elements = []
        for _i in range(int(index[-1]) + 1):
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    elements.append(nums1[0])
                    nums1.pop(0)
                else:
                    elements.append(nums2[0])
                    nums2.pop(0)
            elif nums1:
                elements.append(nums1[0])
                nums1.pop(0)
            else:
                elements.append(nums2[0])
                nums2.pop(0)
        print(elements)
        return sum([elements[int(i)] for i in index]) / len(index)


nums1 = [1, 3]
nums2 = [2]
sln = Solution()
res = sln.findMedianSortedArrays(nums1, nums2)
print(res)
