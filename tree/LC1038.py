"""
给定一个二叉搜索树 root (BST)，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。

提醒一下， 二叉搜索树 满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from data_structure.tree import TreeNode


class Solution:
    total = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return root

    def dfs(self, root, ):
        if not root:
            return

        self.dfs(root.right)
        self.total += root.val
        root.val = self.total
        self.dfs(root.left)
