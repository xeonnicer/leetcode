from collections import deque


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#
#         # 设置滑动窗口队列，window
#         window = deque()
#         max_length = 0
#         # curr_length = 0
#         for i in s:
#             window.append(i)
#             if len(window) == len(set(window)):
#                 max_length = max(max_length,len(window))
#             else:
#                 while len(window) > len(set(window)):
#                     window.popleft()
#         # 已经覆盖了所有元素，return 长度
#         # load 元素，扩张window
#         # 判断是否合规。
#         # 合规，长度加一
#         # 不合规，移动窗口（左边减少1）
#         #
#         return max_length
#

#
# sln = Solution()
# res = sln.lengthOfLongestSubstring("nfpdmpi")
# print(res)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        left = 0
        pool = set()  # 用来判断目前l-r有哪些字符
        for right in range(len(s)):
            if s[right] not in pool:
                pool.add(s[right])
                ans = max(len(pool), ans)
                continue
            while left < right:
                pool.remove(s[left])
                if s[left] == s[right]:
                    left += 1
                    break
                left += 1
            pool.add(s[right])
        ans = max(len(pool), ans)
        return ans


# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = "au"
# s = " "
s = "aab"
ans = Solution().lengthOfLongestSubstring(s)
print(ans)
