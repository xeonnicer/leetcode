"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional, List
from data_structure.tree import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        depth = 0
        visited_depth = []

        def dfs(root):
            nonlocal path
            nonlocal depth
            if not root:
                return
            if depth in visited_depth:
                pass
            else:
                path.append(root.val)
                visited_depth.append(depth)
            depth += 1
            dfs(root.right)
            dfs(root.left)
            depth -= 1

        dfs(root)
        return path
