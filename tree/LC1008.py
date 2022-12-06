# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from data_structure.tree import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        midorder = preorder.copy()
        midorder.sort()

        def dfs(pre, mid):
            if not pre or not mid:
                return None
            root = TreeNode(pre[0])
            left_count = mid.index(pre[0])

            root.left = dfs(pre[1:left_count + 1], mid[:left_count])
            root.right = dfs(pre[left_count + 1:], mid[left_count + 1:])
            return root

        root = dfs(preorder, midorder)
        return root


preorder = [8, 5, 1, 7, 10, 12]
ans = Solution().bstFromPreorder(preorder)
