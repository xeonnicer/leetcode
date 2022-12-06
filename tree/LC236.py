"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         path_p, path_q = self.DFS(root, p, q)
#
#         target = root
#         for i in path_p:
#             for j in path_q:
#                 if i.val == j.val:
#                     target = j
#         return target
#
#     def DFS(self, root, p, q):
#         path_p = []
#         path_q = []
#         target_p_path = []
#         target_q_path = []
#         find_p = False
#         find_q = False
#
#         def helper(root, p, q):
#             nonlocal find_p, find_q
#             if find_p and find_q:
#                 return
#             if not root:
#                 return
#             path_p.append(root)
#             path_q.append(root)
#             if root.val == p.val and not find_p:
#                 nonlocal target_p_path
#                 target_p_path = path_p.copy()
#                 find_p = True
#             if root.val == q.val and not find_q:
#                 nonlocal target_q_path
#                 target_q_path = path_q.copy()
#                 find_q = True
#             helper(root.left, p, q)
#             helper(root.right, p, q)
#             path_p.pop()
#             path_q.pop()
#
#         helper(root, p, q)
#
#         return target_p_path, target_q_path


class Solution:
    ans = None

    def dfs(self, root, p, q):
        if not root:
            return False
        lson = self.dfs(root.left, p, q)
        rson = self.dfs(root.right, p, q)
        if (lson and rson) or (root.val == p.val or root.val == q.val) and (lson or rson):
            self.ans = root
        return (lson or rson) or (root.val == p.val or root.val == q.val)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.ans
