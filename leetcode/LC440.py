class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1  # 偏移量调整，如果k=1,直接返回1
        while k > 0:
            total = self.get_nodes(n, curr)
            if total <= k:
                curr += 1
                k -= total
            else:
                curr *= 10
                k -= 1
        return curr

    def get_nodes(self, n, curr):
        total = 0
        next = curr + 1
        while curr <= n:
            total += min(n - curr + 1, next - curr)
            next *= 10
            curr *= 10
        return total