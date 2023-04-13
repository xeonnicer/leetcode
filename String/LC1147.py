"""
你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:

subtexti 是 非空 字符串
所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立
返回k可能最大值。

 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-chunked-palindrome-decomposition
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestDecomposition(self, text: str) -> int:
        count = 0

        j = len(text) - 1
        i = 0
        _length = 1
        start_idx = i
        while i < j:
            if text[start_idx:start_idx + _length] != text[j:j + _length]:
                i += 1
                j -= 1
                _length += 1
            else:
                i += 1
                j -= 1
                start_idx = i
                _length = 1
                count += 2
        # if _length == 1:
        #     print('length', 1)
        #     pass
        # else:
        #     print('length', _length)
        #     count += 1
        if len(text) % 2 != 0 or _length != 1:
            count += 1
        return count


# text = "ghiabcdefhelloadamhelloabcdefghi"
# print(len(text))
# text = "antaprezatepzapreanta"
# text = "merchant"
# text = "elvtoelvto"
text = 'aaa'
ans = Solution().longestDecomposition(text)
print(ans)
