"""
在一条环路上有 n个加油站，其中第 i个加油站有汽油gas[i]升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1个加油站需要消耗汽油cost[i]升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 gas 和 cost ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。


"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0

        while i < n:
            j = i
            remain = gas[i]
            while remain - cost[j] >= 0:
                remain = remain - cost[j] + gas[(j + 1) % n]
                j = (j + 1) % n
                if j == i:
                    return i
            if j < i:
                return -1
            i = j
            i += 1
        return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
# gas = [2, 3, 4]
# cost = [3, 4, 3]
# gas = [3, 1, 1]
# cost = [1, 2, 2]
ans = Solution().canCompleteCircuit(gas, cost)
print(ans)
