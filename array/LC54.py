"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_index_min = 0
        row_index_max = len(matrix[0]) - 1
        col_index_min = 0
        col_index_max = len(matrix) - 1
        r = row_index_min
        c = col_index_min
        # print(row_index_min, row_index_max, col_index_min, col_index_max)
        res = []
        # 右
        while True:
            #  右
            print('r,c', r, c)
            if r == row_index_min and c == col_index_min:
                for i in range(col_index_max + 1):
                    res.append(matrix[r][c])
                    # print(matrix[r][c])
                    c += 1
                # col index 最小值加1
                row_index_min += 1
            print(res)
            if row_index_min > row_index_max:
                break
            # 下
            c -= 1
            r += 1
            print('r,c', r, c)
            if r == row_index_min and c == col_index_max:
                for i in range(row_index_min, row_index_max + 1):
                    res.append(matrix[r][c])
                    r += 1
                col_index_max -= 1
            print(res)
            if row_index_max < row_index_min:
                break
            # 左
            r -= 1
            c -= 1
            print('r,c', r, c)
            if r == row_index_max and c == col_index_max:
                for i in range(col_index_max, col_index_min - 1, -1):
                    res.append(matrix[r][c])
                    c -= 1
                row_index_max -= 1
            print(res)
            if row_index_max < row_index_min:
                break
            print('1111',row_index_max)
            # 上
            r -= 1
            c += 1
            print('r,c', r, c)
            if r == row_index_max and c == col_index_min:
                for i in range(row_index_max, row_index_min - 1, -1):
                    res.append(matrix[r][c])
                    print(matrix[r][c])
                row_index_max -= 1
            print(res)
            print(row_index_max, row_index_min)
            if row_index_max < row_index_min:
                print(' get in')
                break
        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sln = Solution()
res = sln.spiralOrder(matrix)
print(res)
