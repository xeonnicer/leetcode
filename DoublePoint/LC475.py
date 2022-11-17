"""
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

"""
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters.insert(0, -10000000000)
        heaters.append(10000000000)
        curr_heater = 0  # heater index
        r = 0
        for j in houses:
            for i in range(curr_heater, len(heaters)):
                if heaters[i] > j:
                    r = max(r, min(heaters[i] - j, j - heaters[i - 1]))
                    break
            curr_heater = i
        return r


# houses = [1, 5]
# heaters = [2]
houses = [1, 2, 3, 4]
heaters = [1, 4]
ans = Solution().findRadius(houses, heaters)
print(ans)
