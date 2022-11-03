"""
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：

如果目标字母 target = 'z' 并且字符列表为letters = ['a', 'b']，则答案返回'a'


"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        length = len(letters)
        l = 0
        r = length - 1
        while l < r:
            mid = l + (r - l) // 2
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1
        return letters[l]


letters = ["c","f","j"]
target = "j"

ans = Solution().nextGreatestLetter(letters, target)
print(ans)
