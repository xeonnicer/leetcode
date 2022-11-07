"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""

from typing import List


class Solution:
    def __init__(self):
        self.path = list()
        self.result = list()
        self.all_brackets = {}

    def generateParenthesis(self, n: int) -> List[str]:
        self.all_brackets = {"(": n, ")": n}
        self.backTracing(n=self.all_brackets, k=2 * n, index=0)
        return list(set([''.join(i) for i in self.result]))

    def backTracing(self, n, k, index):

        if len(self.path) == k:
            self.result.append(self.path.copy())
            return
        for i in range(2):
            bracket = self.pick(n, i)
            if not bracket:
                return
            self.path.append(bracket)
            self.backTracing(n, k, i)
            _back = self.path.pop()
            if _back == "(":
                n['('] += 1
            else:
                n[')'] += 1

    def pick(self, all_brackets, index):
        len_left = all_brackets['(']
        len_right = all_brackets[')']
        if index == 0 and len_left > 0:
            all_brackets['('] -= 1
            return '('
        elif index == 1 and len_right and len_left < len_right:
            all_brackets[')'] -= 1
            return ')'
        elif not len_left and len_right:
            all_brackets[')'] -= 1
            return ')'
        else:
            return ''


n = 1
ans = Solution().generateParenthesis(n)
print(len(ans))
print(ans)
