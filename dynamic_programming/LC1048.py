"""
给出一个单词数组 words ，其中每个单词都由小写英文字母组成。

如果我们可以 不改变其他字符的顺序 ，在 wordA 的任何地方添加 恰好一个 字母使其变成 wordB ，那么我们认为 wordA 是 wordB 的 前身 。

例如，"abc" 是 "abac" 的 前身 ，而 "cba" 不是 "bcad" 的 前身
词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word1 是 word2 的前身，word2 是 word3 的前身，依此类推。一个单词通常是 k == 1 的 单词链 。

从给定单词列表 words 中选择单词组成词链，返回 词链的 最长可能长度 。

"""
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        hash_words = {i: i for i in set(words)}
        # longest preWord chain which ending in dp[i]
        dp = {}

        def dfs(word):
            res = 0
            for i in range(len(word)):
                sub_word = word[:i] + word[i + 1:]
                if sub_word in hash_words:
                    if dp.get(word):
                        return dp.get(word)
                    res = max(res, dfs(sub_word))
            dp[word] = res + 1
            return res + 1

        # for word in words:
        #     dfs(word)
        print(dp)
        return max(dfs(word) for word in words)


# words = ["a", "b", "ba", "bca", "bda", "bdca"]
words = ["pcxbcf", "xbc", "xb", "cxbc", "pcxbc"]
ans = Solution().longestStrChain(words)
print(ans)
# a = "pcxbcf"
# for i in range(len(a)):
#     _tmp = a[:i] + a[i + 1:]
#     print(_tmp)
