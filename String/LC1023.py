"""
如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。

"""
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = [False for i in range(len(queries))]
        # print(ans)
        for idx, word in enumerate(queries):
            j = 0
            for i in word:
                if 65 <= ord(i) <= 90:
                    if j == len(pattern):
                        # pattern over, but still uppercase letter, False
                        break
                    # capital letter
                    if pattern[j] == i:
                        # The uppercase letter must be the same as the current first character of pattern
                        j = j + 1 if j <= len(pattern) - 1 else j
                        continue
                    else:
                        break
                else:
                    if j == len(pattern):
                        # pattern over, but still uppercase letter, False
                        continue
                    # lowercase letter
                    if pattern[j] == i:
                        j = j + 1 if j <= len(pattern) - 1 else j
                        continue

            if j == len(pattern) and i == word[-1]:
                # print(idx)
                ans[idx] = True
        return ans


# queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
# pattern = "FB"
# queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
# pattern = "FoBa"
queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaT"


ans = Solution().camelMatch(queries, pattern)
print(ans)
# print(ord("A"))
# print(ord("Z"))
# print(ord("a"))
# print(ord("z"))
