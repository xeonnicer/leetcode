"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from data_structure.tree import TreeNode
from typing import List


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def pre_order(root, path: List):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right and sum(path) == targetSum:
                result.append(path.copy())
            pre_order(root.left, path)
            pre_order(root.right, path)
            path.pop()

        pre_order(root, [])
        return result
