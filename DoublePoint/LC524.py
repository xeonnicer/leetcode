"""
给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        max_length = 0
        dictionary.sort()
        length_s = len(s)
        target = ''
        for d_str in dictionary:
            if len(d_str) > length_s:
                continue
            point_d_str = 0
            match = False
            for i in range(len(s)):
                if s[i] == d_str[point_d_str]:
                    if point_d_str == len(d_str) - 1:
                        match = True
                        break
                    point_d_str += 1
                    continue
            # print(d_str)
            # print(match)
            if match:
                if len(d_str) > max_length:
                    target = d_str
                    max_length = len(d_str)
                # target = d_str if len(d_str) > max_length else ''
        return target


s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]

# s = "abpcplea"
# dictionary = ["a", "b", "c"]

# s = "abpcplea"
# dictionary = ["ale", "apple", "monkey", "plea", "abpcplaaa", "abpcllllll", "abccclllpppeeaaaa"]
ans = Solution().findLongestWord(s, dictionary)
print(ans)

"""

# all str in dict also in  a
            res = all(map(lambda x: True if x in s else False, i))
            if res:
                print(i)
                reverse_res = any(map(lambda x: True if x not in i else False, s))
                print(reverse_res)
                if reverse_res and res:
                    if len(i) > max_length:
                        target = i
                        max_length = len(i)

"""
