# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version == bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l < r:
            mid = l + (r - l) // 2
            print(mid)
            # break
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l

n = 5
bad = 4

ans = Solution().firstBadVersion(n)
print(ans)
