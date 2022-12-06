"""
给定一个不重复的整数数组nums 。最大二叉树可以用下面的算法从nums 递归地构建:

创建一个根节点，其值为nums 中的最大值。
递归地在最大值左边的子数组前缀上构建左子树。
递归地在最大值 右边 的子数组后缀上构建右子树。
返回nums 构建的 最大二叉树 。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
from data_structure.tree import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(None, nums)

    def helper(self, root, help_nums: List[int]):
        # print(help_nums)
        if not help_nums:
            return
        idx = self.get_max_idx(help_nums)
        root = TreeNode(val=help_nums[idx])
        root.left = self.helper(None, help_nums[:idx])
        root.right = self.helper(None, help_nums[idx + 1:])
        return root

    def get_max_idx(self, nums: List[int]):
        return nums.index(max(nums))


nums = [3, 2, 1, 6, 0, 5]
ans = Solution().constructMaximumBinaryTree(nums)
# print(nums[:3])
# print(nums[3:])
