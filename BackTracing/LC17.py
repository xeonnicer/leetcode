"""
17. 电话号码的字母组合
"""

from typing import List


class Solution:
    def __init__(self):
        self.path = list()
        self.result = list()
        self._map = {"2": 'abc',
                     "3": 'def',
                     "4": 'ghi',
                     "5": 'jkl',
                     "6": 'mno',
                     "7": 'pqrs',
                     "8": 'tuv',
                     "9": 'wxyz',
                     }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.backTracing(digits, k=len(digits), startIdx=0)

        return [''.join(i) for i in self.result]

    def backTracing(self, n, k, startIdx):
        if len(self.path) == k:
            # print('get a result return')
            self.result.append(self.path.copy())
            return
        number = n[len(self.path)]
        _choice = self._map.get(number)
        for i in range(0, len(_choice)):
            self.path.append(_choice[i])
            self.backTracing(n, k, i + 1)
            # print(self.path)
            self.path.pop()
            # print(self.path)


digits = "2"
ans = Solution().letterCombinations(digits)
print(ans)
