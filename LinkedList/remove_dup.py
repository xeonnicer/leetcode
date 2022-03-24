from data_structure.linked_list import ListNode
from test_case.linked_list import LinkedListTestCase


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


obj = LinkedListTestCase()
test_case = obj.get_test_case([1, 1, 1])
print(test_case)
sln = Solution()
res = sln.deleteDuplicates(test_case)
print(res)
