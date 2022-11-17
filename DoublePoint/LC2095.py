"""
给你一个链表的头节点 head 。删除 链表的 中间节点 ，并返回修改后的链表的头节点 head 。

长度为 n 链表的中间节点是从头数起第 ⌊n / 2⌋ 个节点（下标从 0 开始），其中 ⌊x⌋ 表示小于或等于 x 的最大整数。

对于 n = 1、2、3、4 和 5 的情况，中间节点的下标分别是 0、1、1、2 和 2 。

"""
from typing import Optional
from data_structure.linked_list import ListNode
from test_case.linked_list import LinkedListTestCase


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        dummyHead = ListNode(0, None)
        dummyHead.next = head
        prev = dummyHead
        if fast.next == None:
            return None
        while fast:
            if fast.next == None:
                break
            if fast.next.next == None:
                prev = prev.next
                slow = slow.next
                break
            fast = fast.next.next
            prev = prev.next
            slow = slow.next
            print(fast.val)
            print(slow.val)
            print(prev.val)
        prev.next = slow.next
        return head


head = [1]
test_case = LinkedListTestCase().get_test_case(head)
point = test_case
# while point:
#     print(point.val)
#     point = point.next
# print('----------------------')
ans = Solution().deleteMiddle(test_case)
point = ans
while point:
    print(point.val)
    point = point.next