"""
给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        n_length = len(needle)
        for idx, i in enumerate(haystack):
            if haystack[idx:idx + n_length] == needle:
                return idx
        return index


# haystack = "sadbutsad"
# needle = "sad"
haystack = "leetcode"
needle = "leeto"


ans = Solution().strStr(haystack, needle)
print(ans)