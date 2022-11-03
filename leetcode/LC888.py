"""
爱丽丝和鲍勃拥有不同总数量的糖果。给你两个数组 aliceSizes 和 bobSizes ，aliceSizes[i] 是爱丽丝拥有的第 i 盒糖果中的糖果数量，bobSizes[j] 是鲍勃拥有的第 j 盒糖果中的糖果数量。

两人想要互相交换一盒糖果，这样在交换之后，他们就可以拥有相同总数量的糖果。一个人拥有的糖果总数量是他们每盒糖果数量的总和。

返回一个整数数组 answer，其中 answer[0] 是爱丽丝必须交换的糖果盒中的糖果的数目，answer[1] 是鲍勃必须交换的糖果盒中的糖果的数目。如果存在多个答案，你可以返回其中 任何一个 。题目测试用例保证存在与输入对应的答案。

"""

from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        # dict_a = {i: i for i in aliceSizes}
        dict_b = {i: i for i in bobSizes}
        for i in aliceSizes:
            target = dict_b.get(i - (sum_a - sum_b) // 2)
            if target:
                return [i, target]


aliceSizes = [1, 2]
bobSizes = [2, 3]
ans = Solution().fairCandySwap(aliceSizes, bobSizes)
print(ans)
