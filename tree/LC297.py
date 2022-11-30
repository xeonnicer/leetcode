from typing import List
from data_structure.tree import TreeNode


class Codec:
    def serialize(self, root):

        return self.rserialize(root, "")

    def deserialize(self, data):
        dataList = data.split(",")

        return self.rdeserialize(dataList)

    def rserialize(self, root, string):
        if not root:
            string += "None,"
        else:
            string += str(root.val) + ","
            string = self.rserialize(root.left, string)
            string = self.rserialize(root.right, string)

        return string

    def rdeserialize(self, dataList: List, ):
        if dataList[0] == 'None':
            dataList.pop(0)
            return None

        root = TreeNode(dataList[0])
        dataList.pop(0)
        root.left = self.rdeserialize(dataList)
        root.right = self.rdeserialize(dataList)

        return root


ans = Codec()