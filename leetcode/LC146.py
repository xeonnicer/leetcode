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


class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return f'Node(key={self.key}, val={self.val})'

    def __repr__(self):
        return f'Node(key={self.key}, val={self.val})'


class BidLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def append_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def append(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def pop_head(self):
        if self.head.next == self.tail:
            return None
        node = self.head.next
        self.remove(self.head.next)
        return node

    def pop(self):
        if self.head.next == self.tail:
            return None
        node = self.tail.prev
        self.remove(self.tail.prev)
        return node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def __str__(self):
        p = self.head.next
        vals = []
        while p.next and p != self.tail:
            vals.append(str((p.key, p.val)))
            p = p.next
        return 'Head <--> ' + ' <--> '.join(vals) + ' <--> Tail'


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.bid = BidLinkedList()

    def get(self, key: int) -> int:
        return self._get(key)

    def put(self, key: int, value: int) -> None:
        return self._put(key, value)

    def _get(self, key):
        node = self.key_map.get(key)
        if node:
            self.make_recent(key)
            return node.val
        return -1

    def _put(self, key, value):
        node = self.key_map.get(key)
        # print('get in _put', key, value, node)
        if node:
            self.remove_key(key)
            self.add_recent(key, value)
            return None
        if self.bid.size == self.capacity:
            self.remove_least_recent()
        self.add_recent(key, value)
        return None

    def make_recent(self, key):
        node = self.key_map.get(key)
        self.bid.remove(node)
        self.bid.append(node)

    def remove_key(self, key):
        node = self.key_map.pop(key)
        self.bid.remove(node)

    def add_recent(self, key, value):
        node = Node(key, value)
        self.key_map.update({key: node})
        self.bid.append(node)

    def remove_least_recent(self):
        node = self.bid.pop_head()
        self.key_map.pop(node.key)


op = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
arg = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
print(len(op), len(arg))
cache = LRUCache(2)
print(None)
for i in range(len(op)):
    attr = getattr(cache, op[i])
    # print('op: ', op[i], *arg[i])
    print('op result:', attr(*arg[i]))
    # print(cache.key_map)
    # print(cache.bid)
    # print(cache.bid.size)
    # print('-----------------------------')
# print(cache.bid)

# print('after op ', op[i], "(", arg[i], ")")
# print(cache._key_map)
# print(cache._value)
# print('-----------------------------')
# bid = BidLinkedList()
# bid.append_head(Node(1, 1))
# bid.append_head(Node(0, 0))
# bid.append(Node(2, 2))
# bid.append(Node(0, 0))
# node = bid.pop_head()
# print(node.val)
# node = bid.pop()
# print(node)
# node = Node(-1, -1)
# bid.append(node)
# print(bid)
# print(node, node.prev, node.next)
# bid.remove(node)
# print(bid)
