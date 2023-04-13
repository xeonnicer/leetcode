# a = "A"
# _map = {}
#
# for index, i in enumerate(range(ord("A"), ord("A") + 26)):
#     _map.update({chr(i): index + 1})
# print(_map)

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         # mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
#         #            'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
#         #            'X': 24, 'Y': 25, 'Z': 26}
#         result = []
#         path = []
#
#         def backTracing(path, arr: str, start_index, pick_length, ):
#             if pick_length > 2:
#                 return
#
#             while arr:
#                 num = arr[:pick_length]
#                 if num.startswith("0"):
#                     return
#                 if int(num) > 26:
#                     return
#                 if num:
#                     path.append(num)
#                 if not arr[pick_length:]:
#                     result.append(path.copy())
#                     print(result)
#                     return
#                 backTracing(path, arr[pick_length:], start_index, pick_length)
#                 # for i in range(pick_length):
#                 #     path.pop()
#                 pick_length += 1
#                 for i in range(min(pick_length, len(path))):
#                     path.pop()
#
#         backTracing(path, s, 0, 1)
#         print(result)
#         return len(result)
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         legalstr = set(str(i) for i in range(1, 27))
#         self.ans = 0
#         def dfs(s):
#             if len(s)==0:
#                 self.ans += 1
#                 return
#             # 对于任何一个字符串，我们每次可以读取一到两个
#             if s[0] in legalstr:
#                 dfs(s[1 : ])
#             if len(s)>1 and s[ : 2] in legalstr:
#                 dfs(s[2 : ])
#             return
#         dfs(s)
#         return self.ans

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if not s:
#             return 1
#         length = len(s)
#         dp = [0 for i in range(length)]
#         dp[0] = 1
#         for i in range(length):
#             if s[i] == "0":
#             else:
#
#             dp[i] =



s = "226"
s = "06"
s = '12'
s = '11106'
s = "1201234"
# ans = Solution().numDecodings(s)
# print(ans)
