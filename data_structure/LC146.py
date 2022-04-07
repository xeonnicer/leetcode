"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._key_map = {}
        self._value = deque(maxlen=capacity)

    def get(self, key: int) -> int:
        return self._get(key)

    def put(self, key: int, value: int) -> None:
        return self._put(key, value)

    def _get(self, key):
        q_index = self._key_map.get(key, -1)
        if q_index != -1:
            # 取回值
            value = self._value[q_index][1]
            # 移动最新使用过的值
            self._mv_recent(key)
            return value
        return -1

    def _put(self, key, value):
        q_index = self._key_map.get(key, -1)
        if q_index != -1:
            # 设置tuple,键：值
            self._value[q_index] = key, value
        else:
            if len(self._value) == self.capacity:
                self._pop_old()
            self._value.append((key, value))
            # q_index = self._value.index(value)
            self._key_map.update({key: len(self._value) - 1})
        return None

    def _pop_old(self):
        key, value = self._value.popleft()
        self._key_map.pop(key)

    def _mv_recent(self, key):
        self._value.append(self._value.popleft())
        self._key_map.update({key:len(self._value) - 1})


op = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
arg = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
print(len(op), len(arg))
cache = LRUCache(2)
print(None)
for i in range(len(op)):
    attr = getattr(cache, op[i])
    print(attr(*arg[i]))
    # print('-----------------------------')
    # print('after op ', op[i], "(", arg[i], ")")
    # print(cache._key_map)
    # print(cache._value)
    # print('-----------------------------')
