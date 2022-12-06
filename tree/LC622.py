# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

from data_structure.tree import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        dep_width = {}

        def dfs(root, tid, depth):
            if not root:
                return
            if not dep_width.get(depth):
                dep_width.update({depth: tid})
            nonlocal ans
            ans = max(ans, tid - dep_width.get(depth) + 1)
            tid = tid - dep_width.get(depth) + 1
            dfs(root.left, tid << 1, depth + 1)
            dfs(root.right, tid << 1 | 1, depth + 1)

        dfs(root, 1, 0)
        return ans
