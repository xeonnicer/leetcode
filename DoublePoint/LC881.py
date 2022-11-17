"""给定数组 people 。people[i]表示第 i 个人的体重 ，船的数量不限，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回 承载所有人所需的最小船数 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/boats-to-save-people
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while (l <= r):
            if (people[l] + people[r] <= limit):
                l += 1
            r -= 1
            count += 1
        return count


people = [1, 2]
limit = 3
people = [3,2,2,1]
limit = 3
ans = Solution().numRescueBoats(people, limit)
print(ans)
