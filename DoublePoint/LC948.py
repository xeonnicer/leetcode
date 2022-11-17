"""
你的初始 能量 为P，初始 分数 为0，只有一包令牌 tokens 。其中 tokens[i] 是第 i 个令牌的值（下标从 0 开始）。

令牌可能的两种使用方法如下：

如果你至少有token[i]点 能量 ，可以将令牌 i 置为正面朝上，失去token[i]点 能量 ，并得到1分 。
如果我们至少有1分 ，可以将令牌 i 置为反面朝上，获得token[i] 点 能量 ，并失去1分 。
每个令牌 最多 只能使用一次，使用 顺序不限 ，不需 使用所有令牌。

在使用任意数量的令牌后，返回我们可以得到的最大 分数 

"""
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) <= 1 and sum(tokens) > power:
            return 0
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        count = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                count += 1
                l += 1
            elif count > 0 and r - l > 0:
                power += tokens[r]
                count -= 1
                r -= 1
            else:
                return count

        return count


tokens = [100, 200]
P = 150

# tokens = [100]
# P = 50
#
tokens = [100, 200, 300, 400]
P = 200
ans = Solution().bagOfTokensScore(tokens, P)
print(ans)
