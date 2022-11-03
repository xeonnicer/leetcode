"""
给你一个整数数组arr，请你检查是否存在两个整数N 和 M，满足N是M的两倍（即，N = 2 * M）。

更正式地，检查是否存在两个下标i 和 j 满足：

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        _map = {i: index for index, i in enumerate(arr)}
        print(_map)
        for i, index in _map.items():
            target_index = _map.get(2 * i)
            if target_index is not None and target_index != index:
                print(2 * i)
                return True
        return False


arr = [0,0]
ans = Solution().checkIfExist(arr)
print(ans)
