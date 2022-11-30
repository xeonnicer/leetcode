class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        data_list = preorder.split(',')
        if len(data_list) == 1 and data_list[0] == '#':
            return True
        if len(data_list) <= 2:
            return False
        stack = []
        for index, i in enumerate(data_list):
            stack.append(i)
            while len(stack) >= 2 and stack[-1] == '#' and stack[-2] == '#':
                stack = stack[:-3]
                stack.append('#')
                if len(stack) == 1 and stack[0] == '#' and index < (len(data_list) - 1):
                    return False
        # print(stack)
        return len(stack) == 1 and stack[0] == '#'


# preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
preorder = "1,#"
# preorder = "1,#,#,#,#"
ans = Solution().isValidSerialization(preorder)
print(ans)
