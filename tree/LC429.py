"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        stack = []
        if not root:
            return []
        path = []
        stack.append(root)
        while stack:
            level = []
            for i in range(len(stack)):

                node = stack.pop(0)
                level.append(node.val)
                if node.children:
                    for i in node.children:
                        stack.append(i)
            path.append(level)
        return path
