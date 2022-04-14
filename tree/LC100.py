"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        res_p = self.get_pre_order(p)
        res_q = self.get_pre_order(q)
        if res_p == res_q:
            return True
        else:
            return False

    def get_pre_order(self, root):
        res = []
        self.pre_order(root, res)
        return res

    def pre_order(self, root, res):
        if not root:
            res.append(None)
            return
        res.append(root.val)
        self.pre_order(root.left, res)
        self.pre_order(root.right, res)
