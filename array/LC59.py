"""给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        start_row = 0
        start_col = 0
        offset = 1  # last item will be process in next side
        count = 1
        matrix = [[0] * n for i in range(n)]
        for loop in range(n // 2):
            r = start_row
            c = start_col
            for i in range(start_col, n - offset):
                matrix[r][c] = count
                count += 1
                c += 1
            # for i in matrix:
            #     print(i)
            # print('-------------')
            for i in range(start_row, n - offset):
                matrix[r][c] = count
                count += 1
                r += 1
            # for i in matrix:
            #     print(i)
            # print('-------------')
            for i in range(r, start_col, -1):
                matrix[r][c] = count
                count += 1
                c -= 1
            # for i in matrix:
            #     print(i)
            # print('-------------')
            for i in range(r, start_row, -1):
                matrix[r][c] = count
                count += 1
                r -= 1
            # for i in matrix:
            #     print(i)
            # print('-------------')
            # start to next loop
            # for i in matrix:
            #     print(i)
            start_row += 1
            start_col += 1
            offset += 1
        if n % 2 != 0:
            matrix[start_row][start_col] = count
        return matrix


n = 3

ans = Solution().generateMatrix(n)
print('answer: -------')
for i in ans:
    print(i)
