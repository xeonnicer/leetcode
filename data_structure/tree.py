class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # return preOrder(self)
        return str(self.val)

    def __repr__(self):
        return self.__str__()

    def pre_order_display(self):
        return preOrder(self)


def preOrder(root: TreeNode) -> str:
    path = []

    def preOrderHelper(root: TreeNode):
        if not root:
            path.append(None)
            return
        else:
            path.append(root.val)
        if not root.left and not root.right:
            return
        preOrderHelper(root.left)
        preOrderHelper(root.right)

    preOrderHelper(root)

    return str(path)
