'''
Doubly Linked List
Hashmap

Back to Back SWE: https://youtu.be/S6IfqDXWa10
'''


class ListNode:
    '''
    node def of a boubly linked list
    each node not only has value, but also has key
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None  # points to the previous node
        self.next = None  # points to the next node


class LRUCache:
    '''
    This cache has two data structures:
    Hashmap:
    Doubly linked list:
    '''

    def __init__(self, max_capacity=0):
        self.max_capacity = max_capacity
        self.total_items_in_cache = 0
        self.hash_table = {}  # <int, ListNode>
        # Dummy head and tail nodes to avoid empty states
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        # Wire the head and tail together
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        '''
        get a value with the key
        as this node has been accesse, we move it to the front of the list
        '''
        node = self.hash_table.get(key, None)
        if node is None:
            return None

        # item has been accessed, so we move it to the front of the cache
        self.move_to_head(node)

        return node.value

    def put(self, key, value):
        '''
        add a new item to the cache
        if the key already exists, then just update the item
        '''
        node = self.hash_table.get(key, None)

        # key does not exist
        if not node:
            new_node = ListNode(key, value)
            self.hash_table[key] = new_node

            # just accessed, add it to the front
            self.add_to_front(new_node)
            self.total_items_in_cache += 1

            # over capacity, remove the LRU item
            if self.total_items_in_cache > self.max_capacity:
                self.remove_lru_entry()

        # key already exists, update the value
        # also move it to the front
        node = self.hash_table[key]
        node.value = value
        self.move_to_head(node)

    def remove_lru_entry(self):
        '''
        remove the LRU entry, which is at the tail of the list
        also we need to remove the related key from hashmap
        '''
        lru_item = self.tail.prev
        self.remove_from_list(lru_item)
        del self.hash_table[lru_item.key]
        self.total_items_in_cache -= 1

    def add_to_front(self, node):
        '''
        add a node to the front
        '''
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_from_list(self, node):
        '''
        remove a node from the list
        '''
        saved_prev = node.prev
        saved_next = node.next

        saved_prev.next = saved_next
        saved_next.prev = saved_prev

    def move_to_head(self, node):
        '''
        remove a node from the list and add it to the front
        '''
        self.remove_from_list(node)
        self.add_to_front(node)

    def inspect_cache(self):
        '''
        print out the hash table
        print all keys in the list int its order
        '''
        for key, node in self.hash_table.items():
            print(f'key: {key}, node: {{{node.key}: {node.value}}}')

        current = self.head
        while current.next.next:
            current = current.next
            print(current.key)


cache = LRUCache(5)

cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)
cache.put(4, 40)
cache.put(5, 50)      # 越後面放的會被擺在 list 越前面
cache.inspect_cache()

print('GET 1: ', cache.get(1))   # key 為 1 的 node 會跑到最前面
cache.inspect_cache()

print('GET 3: ', cache.get(3))   # key 為 3 的 node 會跑到最前面
cache.inspect_cache()

cache.put(1, 100)  # 1 已經存在 只update 並搬到最前面
cache.inspect_cache()

cache.put(12, 120)  # 新的 key  被加進 hashmap 並且放 list 最前面  最舊的 2 會被移除
cache.inspect_cache()

cache.put(6, 60)  # 新的 key  被加進 hashmap 並且放在 list 最前面  最舊的 4 會被移除
cache.inspect_cache()

print('GET 4: ', cache.get(4))  # key 為 4 的 node 已不存在
