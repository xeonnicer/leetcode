# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from typing import List


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self._dfs(nestedList, self.stack)
        print(self.stack)

    def next(self) -> int:
        if self.hasNext():
            return self.stack.pop(0)
        else:
            raise StopIteration

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _dfs(self, nestedList, stack):
        for i in nestedList:
            if i.isInteger():
                stack.append(i.getInteger())
            else:
                self._dfs(i.getList(), stack)


# Your NestedIterator object will be instantiated and called as such:


# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


nestedList = [[1, 2, [3]], [1, 2, 3], [1, [[[[3]]]]]]
nestedList = [[1, 1], 2, [1, 1]]
iterator = NestedIterator(nestedList)
res = []

while iterator.hasNext():
    res.append(iterator.next())
print(res)
