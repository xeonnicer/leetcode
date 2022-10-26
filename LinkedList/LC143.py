# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from data_structure.linked_list import ListNode
from test_case.linked_list import LinkedListTestCase


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p = head
        cache = []
        pre = None
        pnext = None
        while p:
            pnext = p.next
            cache.append((p, pre, pnext))
            pre = p
            p = p.next
        if len(cache) < 3:
            return head
        cache = cache[-1: int(-len(cache) / 2) - 1: -1]
        index = 0
        p = head
        while p:
            if index < len(cache):
                # print('get in')
                # if index % 2 == 0:
                cache[index][0].next = p.next
                p.next = cache[index][0]
                p = p.next.next
                index += 1
            else:
                p.next = None
                break
        return head

case = [1, 2, 3, 4, 5]
tc = LinkedListTestCase()
linked_list = tc.get_test_case(case)
cache = []
p = linked_list

pre = None
pnext = None
while p:
    pnext = p.next
    cache.append((p, pre, pnext))
    pre = p
    p = p.next
print(cache)
cache = cache[-1: int(-len(cache) / 2) - 1: -1]
print(cache)

index = 0
p = linked_list
while p:
    if index < len(cache):
        # print('get in')
        # if index % 2 == 0:
        cache[index][0].next = p.next
        p.next = cache[index][0]
        p = p.next.next
        index += 1
    else:
        p.next = None
        break
p = linked_list
print('--------------')
while p:
    print(p)
    p = p.next
