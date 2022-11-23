"""
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
"""
from typing import List
from data_structure.tree import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
#         if n == 1:
#             return [TreeNode(val=1)]
#         pass
#         path = []
#         result = []
#         picking = [i for i in range(1, n + 1)]
#
#         def backTracing(n, k, index):
#             if not n:
#                 # 存入根节点
#                 result.append(path[0])
#                 return
#             for i in range(len(n) - 1):
#                 tree = TreeNode(val=n[i])
#                 if not path:
#                     path.append(tree)
#                 else:
#                     path.append(tree)
#                     if n[i] > path[-1].val:
#                         path[-2].right = tree
#                     else:
#                         path[-2].left = tree
#                 _tmp = n.copy()
#                 _tmp.pop(_tmp.index(n[i]))
#                 backTracing(_tmp, k, i)
#                 path.pop()
#
#         backTracing(picking, n, 1)
#         return result

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None, ]

            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)

                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)

                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []


n = 3
ans = Solution().generateTrees(3)
print(ans)
