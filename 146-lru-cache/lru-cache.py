# Time complexity: O(1) and Space complexity: O(n)
class LRUCache:
    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.next = None
            self.previous = None


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheDict = {}

        self.left = self.Node()
        self.right = self.Node()

        self.left.next = self.right
        self.right.previous = self.left

    def removal(self, node):
        prevNode = node.previous
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.previous = prevNode

    def insert(self, node):
        tail = self.right.previous
        tail.next = node
        node.next = self.right
        node.previous = tail
        self.right.previous = node
        
    def get(self, key: int) -> int:
        if key not in self.cacheDict:
            return -1

        node = self.cacheDict[key]
        self.removal(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cacheDict:
            node = self.cacheDict[key]
            self.removal(node)
            node.value = value
            self.insert(node)
        else:
            node = self.Node(key, value)
            self.insert(node)
            self.cacheDict[key] = node

            if len(self.cacheDict) > self.capacity:
                lru = self.left.next
                self.removal(lru)
                del self.cacheDict[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)