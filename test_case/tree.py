from data_structure.tree import TreeNode
from test_case.base_case import BaseCase


class LinkedListTestCase(BaseCase):
    def get_test_case_from_level_order(self, elements=list()):
        dummy_head = ListNode(-1)
        curr = dummy_head
        for i in elements:
            node = ListNode(i)
            curr.next = node
            curr = node
        test_case = dummy_head.next
        return test_case
