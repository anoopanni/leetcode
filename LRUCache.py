# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/description/


class Node:

    def __init__(self, key = 0, val=0, next=None, prev=None) -> None:
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def print_ll(self, root=None):
        while root:
            print(root.val)
            root = root.next 

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Left - Most recently used and Right - Least recently used
        self.left, self.right = Node(val=-1), Node(val=-2)
        self.left.next, self.right.prev = self.right, self.left
        self.map = {}
        # Test code
        # self.print_ll(self.left)
        # n = Node(1)
        # self.insert(n)
        # self.print_ll(self.left)
        # self.remove(n)
        # self.print_ll(self.left)

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        # self.print_ll(self.left)
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            self.map[key].val = value
        else:
            if self.capacity == 0:
                del self.map[self.left.next.key]
                self.remove(self.left.next)
                self.capacity += 1
            self.map[key] = Node(key, value)
            self.insert(self.map[key])
            self.capacity -= 1

    # Remove the node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert from the right - More Frequently used
    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)





# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
