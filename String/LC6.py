import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        row = numRows
        col = (numRows - 2 + 1) * math.ceil(len(s) / numRows)
        arr = [[""] * col for i in range(row)]

        r = l = 0

        direct = False
        for i in range(len(s)):
            # x = 0,转向向下
            # x = numRows-1 ,转为向上
            arr[r][l] = s[i]
            # for i in arr:
            #     print(i)
            if r == 0:
                direct = False
            elif r == numRows - 1:
                direct = True
            r, l = (r - 1, l + 1) if direct else (r + 1, l)

            # print('------------------------')
        return ''.join(ch for row in arr for ch in row if ch)


s = "PAYPALISHIRING"
s = "ABC"
numRows = 2
ans = Solution().convert(s, numRows)
print(ans)
