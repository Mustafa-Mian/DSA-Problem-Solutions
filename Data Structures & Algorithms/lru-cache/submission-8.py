class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def erase(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        old_mru = self.right.prev
        old_mru.next = node
        node.prev = old_mru
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        val = self.cache[key].val
        self.erase(self.cache[key])
        self.insert(self.cache[key])
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.erase(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            toRemove = self.left.next
            removeKey = toRemove.key
            self.erase(toRemove)
            self.cache.pop(removeKey)
        
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None