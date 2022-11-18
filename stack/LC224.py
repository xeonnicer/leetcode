"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
"""

from operator import add, sub
from typing import List


# Double stack
class Solution:
    opr_map = {
        '+': add,
        '-': sub,
    }

    def calculate(self, s: str) -> int:
        print('s:', s)
        s = s.replace(' ', '').replace('(-', '(0-').replace('(+', '(0+')
        if s.startswith('+') or s.startswith('-'):
            s = '0' + s
        ops = []
        nums = []
        tmp_num = 0
        print('new s: ', s)
        i = 0
        while i < len(s):
            # for i in range(len(s)):
            if s[i] == '(':
                # print('fork: ( ')
                ops.append(s[i])
            elif s[i] == ')':
                # print('fork: )')
                while ops:
                    if ops[-1] != '(':
                        self.cal_stack_until_ops_none(ops, nums)
                    else:
                        ops.pop()
                        break # new code1
                if ops and ops[-1] != '(':
                    # code01
                    self.cal_stack_until_ops_none(ops, nums)
            elif s[i].isdigit():
                # print('fork: digit')
                # input num which maybe more 10
                while s[i].isdigit():
                    tmp_num = tmp_num * 10 + int(s[i])
                    i += 1
                    if i == len(s):
                        break
                nums.append(tmp_num)
                # restore tmp_num
                tmp_num = 0
                if i == len(s):
                    # get last num, cal then return
                    print('get in')
                    self.cal_stack_until_ops_none(ops, nums)
                i -= 1
            elif s[i] in ['+', '-']:
                # if i > 0 and s[i-1] == '(' or s[i-1] == '+' or s[i-1] == '-':
                # print('fork: + / -')
                while ops:
                    if ops[-1] == '(':
                        break
                    self.cal_stack_until_ops_none(ops, nums)
                ops.append(s[i])
            else:
                print('error')
                print(s[i])
                print(s)
            i += 1
        # 可以在最后再补充运算一次也可以在code01位置运算一次，因为，最后可能剩余一组运算符没有处理
        # if ops:
        #     self.cal_stack_until_ops_none(ops, nums)
        print(ops)
        print(nums)
        return int(nums[-1])

    def cal_stack_until_ops_none(self, ops: List, nums: List):
        if not ops or len(nums) < 2:
            return

        # print('ops from cal:', ops)
        # print('nums from cal:', nums)
        opr = ops.pop()
        opr = self.opr_map.get(opr)
        num1 = float(nums.pop())
        num2 = float(nums.pop())
        nums.append(opr(num2, num1))


# s = "(1+(4+5+2)-3)+((6)+18)"  # 33
# s = "1 + 1"                # 2
# s = " - 1 + 2 - 1"          # 0
# s = "-1 + (-1+2 )"          # 0
# s = "2147483647"             # 2147483647
# s = '10+5'                   # 15
# s = "(1)-(5)"               #  -4
# s = "1-(5)"               #  -4
# s = '10 + 5 -( 1+2)'         # 12
# s = '(10) + 5 -( 1+2)'         # 12
# s = '(10 + 5) -( 1+2)'         # 12
# s = '(10 + 5 -( 1+2))'         # 12
s = '(10 + 5 - 1+2)'         # 16
# s = "2-4-(8+2-6+(8+4-(1)+8-10))"  # -15
ans = Solution().calculate(s)
print(ans)
