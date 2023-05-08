"""
2432. 处理用时最长的那个任务的员工
共有 n 位员工，每位员工都有一个从 0 到 n - 1 的唯一 id 。

给你一个二维整数数组 logs ，其中 logs[i] = [idi, leaveTimei] ：

idi 是处理第 i 个任务的员工的 id ，且
leaveTimei 是员工完成第 i 个任务的时刻。所有 leaveTimei 的值都是 唯一 的。
注意，第 i 个任务在第 (i - 1) 个任务结束后立即开始，且第 0 个任务从时刻 0 开始。

返回处理用时最长的那个任务的员工的 id 。如果存在两个或多个员工同时满足，则返回几人中 最小 的 id 。
"""
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        min_id = logs[0][0]
        max_period = logs[0][1]
        for i in range(1, len(logs)):
            period = logs[i][1] - logs[i - 1][1]
            if period > max_period:
                max_period = period
                min_id = logs[i][0]
            elif period == max_period:
                min_id = min(logs[i][0], min_id)
        return min_id


# n = 10
# logs = [[0, 3], [2, 5], [0, 9], [1, 15]]
# n = 26
# logs = [[1, 1], [3, 7], [2, 12], [7, 17]]
n = 2
logs = [[0, 10], [1, 20]]
ans = Solution().hardestWorker(n, logs)
print(ans)
