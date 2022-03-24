"""
1491. 去掉最低工资和最高工资后的工资平均值
给你一个整数数组salary，数组里每个数都是 唯一的，其中salary[i] 是第i个员工的工资。

请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(salary.sort()[1:-1])
