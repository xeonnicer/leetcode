__all__ = ('LRUCache',)


# Definition for LRUCache list.
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

    def move_to_tail(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def __str__(self):
        p = self.head.next
        vals = []
        while p.next and p != self.tail:
            vals.append(str((p.key, p.val)))
            p = p.next
        return 'Head <--> ' + ' <--> '.join(vals) + ' <--> Tail'


class Storage:
    def __init__(self, size):
        self.size = size
        self.mapping = {}
        self.bid_linked_list = BidLinkedList()
        self.head = None
        self.tail = None

    def put(self, key, value):
        node = self.mapping.get(key)
        if node:
            node.val = value
            self.bid_linked_list.move_to_tail(node)
        else:
            node = Node(key, value)
            self.mapping.update({key: node})
            self.bid_linked_list.append(node)
            # print('bid size',self.bid_linked_list.size)
            if self.bid_linked_list.size > self.size:
                node = self.bid_linked_list.pop_head()
                self.mapping.pop(node.key)

    def get(self, key):
        node = self.mapping.get(key)
        if node:
            self.bid_linked_list.move_to_tail(node)
            return node.val
        else:
            return -1


class LRUCache:
    def __init__(self, size, ):
        self.storage = Storage(size)

    def put(self, key, value):
        self.storage.put(key, value)
        return None

    def get(self, key):
        return self.storage.get(key)


if __name__ == '__main__':
    # cache = LRUCache(2)
    # cache.put(1, 1)
    # print(cache.storage.bid_linked_list)
    # cache.put(2, 2)
    # print(cache.storage.bid_linked_list)
    # res = cache.get(1)
    # print(cache.storage.bid_linked_list)
    # print(res)
    # #
    # cache.put(3,3)
    # print('put 3',cache.storage.bid_linked_list)
    # res = cache.get(2)
    # print('get 2',cache.storage.bid_linked_list)
    # print('get 2',res)
    # cache.put(4,4)
    # res = cache.get(1)
    # print('get 1', res)
    # res = cache.get(3)
    # print('get 3', res)
    # res = cache.get(4)
    # print('get 4', res)
    '---------------'
    cache = LRUCache(2)
    cache.put(2,1)
    print(cache.storage.bid_linked_list)
    cache.put(1,1)
    print(cache.storage.bid_linked_list)
    cache.put(2,3)
    print(cache.storage.bid_linked_list)
    cache.put(4,1)
    print(cache.storage.bid_linked_list)
    cache.get(1)
    print(cache.storage.bid_linked_list)
    cache.get(2)
    print(cache.storage.bid_linked_list)