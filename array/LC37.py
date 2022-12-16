"""
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法且不使用额外空间来解决此问题。

"""
import binascii
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        binary = [0 for i in range(32)]
        for i in range(32):
            count = 0
            for j in range(len(nums)):
                count += (nums[j] >> i) & 1
            # print('count', count)
            if count % 3 == 1:
                binary[i] = 1
                # print(res)
        binary.reverse()
        binary = ''.join((str(i) for i in binary)).strip('0')

        return int(binary, base=2)


# nums = [2, 2, 3, 2]
# nums = [0, 1, 0, 1, 0, 1, 99]
nums = [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]
ans = Solution().singleNumber(nums)
print(ans)
# res = 0
# # res |= 1 << 3
# res |= 1 << 2
# print(res)
# res |= 1 << 3
# print(res)
# print(2 ** 32)
