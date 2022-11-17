from typing import List
from collections import deque


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # big top heap
        self.heap = deque()
        self.k = k
        self._init(nums)

    def _init(self, nums):
        for i in nums:
            self._add(i)

    def _add(self, i: int):
        if not self.heap:
            self.heap.append(i)
        elif i < self.heap[0]:
            self.heap.append(i)
        else:
            self.heap.appendleft(i)

    def add(self, val: int) -> int:
        self._add(val)
        return self.heap[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import heapq
k = 3
nums = [4, 5, 8, 2]
kth = KthLargest(k, nums)
print(kth.heap)
print(kth.add(3))
print(kth.heap)
print(kth.add(5))
print(kth.add(10))
print(kth.add(9))
print(kth.add(4))
