"""
给你一个字符串 path ，表示指向某一文件或目录的Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。
在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..）表示将目录切换到上一级（指向父目录）；
两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。
对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。

请注意，返回的 规范路径 必须遵循下述格式：

始终以斜杠 '/' 开头。
两个目录名之间必须只有一个斜杠 '/' 。
最后一个目录名（如果存在）不能 以 '/' 结尾。
此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
返回简化后得到的 规范路径 。

"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path.startswith('/'):
            path = '/' + path
        if not path.endswith('/'):
            path = path + '/'
        if path == '/':
            return '/'
        length = len(path)
        stack = []
        start_i = 0
        multi_slash = False
        for index, i in enumerate(path):
            if path[index] == '/':
                if index == length - 1:  # last '/'
                    pass
                elif path[index + 1] == '/':
                    continue
                name = path[start_i:index + 1]
                name = name.rstrip('/')
                name += '/'
                if name == './':
                    pass
                elif name == '../' or name == '..':
                    if len(stack) > 1:
                        stack.pop(-1)
                else:
                    stack.append(name)
            else:
                if path[index - 1] == '/':
                    start_i = index
        res = ''.join(stack)
        return res.rstrip('/') if len(res) > 1 else res


# path = "/home//foo/"
# path = "/../"
# path = "/home/"
# path = "/a/./b/../../c/"
path = "/a//b////c/d//././/.."
ans = Solution().simplifyPath(path)
print(ans)
