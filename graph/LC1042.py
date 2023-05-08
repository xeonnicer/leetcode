"""
有 n 个花园，按从 1 到 n 标记。另有数组 paths ，其中 paths[i] = [xi, yi] 描述了花园 xi 到花园 yi 的双向路径。在每个花园中，你打算种下四种花之一。

另外，所有花园 最多 有 3 条路径可以进入或离开.

你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。

以数组形式返回 任一 可行的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1、2、3、4 表示。保证存在答案。

"""
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for path in paths:
            adj[path[0] - 1].append(path[1] - 1)
            adj[path[1] - 1].append(path[0] - 1)
        print(adj)
        gards = [0 for i in range(n)]
        for index, path in enumerate(adj):
            for i in range(1, 5):
                if i not in [gards[j] for j in path]:
                    gards[index] = i
                    break
        return gards


# n = 3
# paths = [[1, 2], [2, 3], [3, 1]]
n = 4
paths = [[1, 2], [3, 4]]
ans = Solution().gardenNoAdj(n, paths)
print(ans)
