"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
from data_structure.linked_list import ListNode
from typing import List, Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        dummyHead = ListNode()
        pWork = dummyHead
        while p1 or p2:
            if p1 and p2:
                if p1.val <= p2.val:
                    pWork.next = p1
                    p1 = p1.next
                else:
                    # print('p2',p2)
                    pWork.next = p2
                    p2 = p2.next
            elif p1:
                # print('only p1 ok')
                pWork.next = p1
                p1 = p1.next
            elif p2:
                pWork.next = p2
                p2 = p2.next
            pWork = pWork.next

        return dummyHead.next


from test_case.linked_list import LinkedListTestCase

list1 = LinkedListTestCase().get_test_case([1, 2,4])
list2 = LinkedListTestCase().get_test_case([1, 3, 4])
ans = Solution().mergeTwoLists(list1, list2)
print('------------')
while ans:
    print(ans.val)
    ans = ans.next
