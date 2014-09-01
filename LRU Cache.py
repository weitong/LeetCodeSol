#/usr/bin/env python

# Author: Wei Tong <0day.wei@gmail.com>
#
class LRUCache:
    class Node:
        def __init__(self, k, v):
            self.key = k
            self.value = v
            self.next = None
            self.prev = None

    class DLL:
        def __init__(self, c):
            self.capacity = c
            self.count = 0
            self.head = LRUCache.Node(0, 0)
            self.last = LRUCache.Node(0, 0)
            self.head.next = self.last
            self.last.prev = self.head
            
    # @param capacity, an integer
    def __init__(self, capacity):
        self.dll = LRUCache.DLL(capacity)
        self.nmap = {}

    def __attach(self, node):
        node.prev = self.dll.head
        node.next = self.dll.head.next
        self.dll.head.next.prev = node
        self.dll.head.next = node

    def __detach(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    # @return an integer
    def get(self, key):
        if key in self.nmap:
            n = self.nmap[key]
            if n.prev != self.dll.head:
                self.__detach(n)
                self.__attach(n)
            return n.value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.nmap:
            n = LRUCache.Node(key, value)
            if self.dll.capacity != self.dll.count:
                self.dll.count += 1
            else:
                del(self.nmap[self.dll.last.prev.key])
                self.__detach(self.dll.last.prev)
            self.__attach(n)
            self.nmap[key] = n
        else:
            n = self.nmap[key]
            n.value = value
            self.__detach(n)
            self.__attach(n)
            
if __name__ == "__main__":
    lru = LRUCache(10)
    lru.set(1, 10)
    lru.set(1, 20)
    for i in range(12):
        lru.set(i, i * 10)
    
    print lru.get(1)
