import re


# class Solution:
#     def reverseWords(self, s: str) -> str:
#         l = re.split("\W+", s.strip())
#         # print(l)
#         return ' '.join(l[::-1])

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        slow = 0
        for fast in range(len(s) - 1):
            if s[fast] != " ":
                # if slow == 0:
                # 第一个单词
                s[slow] = s[fast]
                slow += 1
            elif slow != 0 and s[slow - 1] != " ":
                s[slow] = " "
                slow += 1
        s = s[:slow - 1]
        return ''.join(s[:slow])


s = "the sky is blue"
s = "  hello    world  "
ans = Solution().reverseWords(s)
print(ans, "-")
print(len(ans))
# print(s)
