"""
给定一棵二叉树的根 root，请你考虑它所有从根到叶的路径：从根到任何叶的路径。（所谓一个叶子节点，就是一个没有子节点的节点）

假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为「不足节点」，需要被删除。

请你删除所有不足节点，并返回生成的二叉树的根。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from data_structure.tree import TreeNode


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        def dfs(root, parent_sum):
            """
            True  delete
            False keep
            :param root:
            :return:
            """
            if not root:
                return
            curr_sum = parent_sum + root.val
            if root.left == None and root.right == None and curr_sum < limit:
                return True

            l = dfs(root.left, curr_sum)
            r = dfs(root.right, curr_sum)

            if l:
                root.left = None
            if r:
                root.right = None

            if (l and r == None) or (r and l == None) or (l and r):
                return True
            return False

        if dfs(root, 0):
            return None
        else:
            return root


[1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14]
1

[10, 5, 10]
21
