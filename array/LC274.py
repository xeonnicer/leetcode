from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 1:
            return 0 if citations[0] == 0 else 1
        h = 0
        for i in range(n + 1):  # 遍历h
            bigger = 0
            smaller = 0
            for j in citations:
                if j >= i:
                    bigger += 1
                elif j <= i:
                    smaller += 1
            if bigger >= i:
                h = max(h, i)
        return h


# citations = [3, 0, 6, 1, 5]
# citations = [1,3,1]
# citations = [1]
# citations = [0, 1]
# citations = [11, 15]
citations = [1, 2]
# citations = [0, 1, 0]
ans = Solution().hIndex(citations)
print(ans)
