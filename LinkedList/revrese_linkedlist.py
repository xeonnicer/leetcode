from data_structure.linked_list import ListNode
from test_case.linked_list import LinkedListTestCase


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        curr = head
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        # 当curr指向null时，循环跳出，此时pre指向新链表的第一个节点
        return pre


print('test_case:')
print(test_case)
print('answer:')
sln = Solution()
res = sln.reverseList(test_case)
print(res)
