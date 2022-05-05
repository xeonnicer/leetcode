"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from data_structure.linked_list import ListNode
from test_case.linked_list import LinkedListTestCase


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        p = l1
        while p:
            print('1')
            num1.append(str(p.val))
            p = p.next

        num1 = int(''.join(num1[::-1]))
        num2 = []
        p = l2
        while p:
            num2.append(str(p.val))
            p = p.next

        num2 = int(''.join(num2[::-1]))
        num3 = num1 + num2
        num3 = str(num3)[::-1]
        dummy_head = ListNode(-1)
        curr = dummy_head
        for i in num3:
            node = ListNode(i)
            curr.next = node
            curr = node
        test_case = dummy_head.next
        return test_case


case = LinkedListTestCase()
l1 = case.get_test_case([2, 4, 3])
l2 = case.get_test_case([5, 6, 4])
sln = Solution()
res = sln.addTwoNumbers(l1, l2)
print(res)
