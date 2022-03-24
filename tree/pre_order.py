"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
"""

from typing import Optional, List
from data_structure.tree_node import TreeNode



class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cache = []
        self.pre_ordr(root, cache)
        return cache

    def pre_order(self, root, cache):
        if not root:
            return
        cache.append(root.val)
        self.pre_order(root.left, cache)
        self.pre_order(root.right, cache)
