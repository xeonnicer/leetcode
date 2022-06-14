"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        direction = 1
        queue = [root]
        # queue = deque()
        # queue.append(root)
        while queue:
            curr_level = []
            next_level = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                curr_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue.extend(next_level)
            if direction > 0:
                result.append(curr_level)
            else:
                result.append(curr_level[::-1])
            direction *= -1

        return result
