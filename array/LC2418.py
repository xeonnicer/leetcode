from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair = [(i, index) for index, i in enumerate(heights)]

        pair = sorted(pair, key=lambda x: x[0], reverse=True)

        return [names[index] for i, index in pair]


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
ans = Solution().sortPeople(names, heights)
print(ans)
