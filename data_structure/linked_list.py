__all__ = ('ListNode',)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        # return f'ListNode( {self.val}, {self.next} )'
        return str(self.val)

    def __str__(self):
        return str(self.val)

    # @staticmethod
    def display_from_current(self):
        path = []
        work = self
        while work:
            path.append(work.val)
            work = work.next
        return ' -> '.join(str(i) for i in path)
