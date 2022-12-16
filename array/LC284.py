class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.itr = iterator
        self.register = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        self.register = self.register if self.register else self.itr.next()
        return self.register

    def next(self):
        """
        :rtype: int
        """
        ret = self.register if self.register else self.itr.next()
        self.register = None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.register is not None or self.itr.hasNext()
