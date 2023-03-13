class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)

        for i in range(0, len(l), 2 * k):
            l[i:i + k] = list(l[i:i + k])[::-1]

        return "".join(l)


# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         t = list(s)
#         for i in range(0, len(t), 2 * k):
#             t[i: i + k] = reversed(t[i: i + k])
#         return "".join(t)


s = 'abcdefg'
k = 2
s = 'abcdefghijklmn'
ss = 'abcdef ghijkl mn'
k = 3
s = Solution().reverseStr(s, k)
print(s)
