class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.key_map = {}
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.capacity = capacity
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def erase(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        orig_mru = self.mru.prev
        orig_mru.next = node
        node.prev = orig_mru
        node.next = self.mru
        self.mru.prev = node

    def get(self, key: int) -> int:
        if key in self.key_map:
            val = self.key_map[key].value
            self.erase(self.key_map[key])
            self.insert(self.key_map[key])
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            self.erase(self.key_map[key])
        self.key_map[key] = Node(key, value)
        self.insert(self.key_map[key])

        if self.capacity < len(self.key_map):
            self.key_map.pop(self.lru.next.key)
            self.erase(self.lru.next)

