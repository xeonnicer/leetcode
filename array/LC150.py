"""
根据 逆波兰表示法，求表达式的值。

有效的算符包括+、-、*、/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

注意两个整数之间的除法只保留整数部分。

可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

"""
from typing import List

from operator import add, sub, mul, truediv

opr_map = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv

}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                # func = opr_map.get(i)
                _ans = opr_map.get(i)(num1, num2)
                stack.append(_ans)
            else:
                stack.append(i)
        return stack[0]


tokens = ["2", "1", "+", "3", "*"]
# tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
ans = Solution().evalRPN(tokens)
print(ans)
