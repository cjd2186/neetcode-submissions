#need doubly linked list to remove nodes easily
class Node:
    def __init__(self, key, val, prev = None, nxt = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.nxt = nxt

class LRUCache:
#LRU --> replace least access item with new item
#O(1) get/put
# newest node <--> oldest node
# get --> hard part
## search -> 
## eviction -> remove tail of linked list
# put --> 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currentCap = 0
        # {key : node}
        self.keys = {}
        #dummy head/tail
        self.head = Node(-1, 0)
        self.tail = Node(-1, 0, prev=self.head)
        self.head.nxt = self.tail

    #when something is accessed, move it to the head!
    def get(self, key: int) -> int:
        node = self.keys.get(key, None)
        if not node:
            print("NONE")
            return -1
        else:
            if self.head.nxt == node:
                return node.val

            #remove node from list
            prev_node = node.prev
            node.nxt.prev = node.prev
            prev_node.nxt = node.nxt
            
            self.insert_head(node.key, node.val)
            return node.val

    #add or update node in list
    #use dictionary to find node like we do in get
    def put(self, key: int, value: int) -> None:
        # update to linked list and dict:
        if self.keys.get(key, None):
            print("UPDATE")
            #move to head
            pop_node = self.keys[key]
            pop_prev = pop_node.prev
            pop_node.prev.nxt = pop_node.nxt
            pop_node.nxt.prev = pop_prev
            self.insert_head(key, value)
            self.keys[key].val = value
            
            return
        #check if you need to delete last node
        if self.currentCap + 1 > self.capacity:
            print("POP")
            pop_key = self.tail.prev.key
            # 3 <-> 4 <-> TAIL
            tail_prev = self.tail.prev.prev
            self.tail.prev.prev.nxt = self.tail
            self.tail.prev = tail_prev
            self.keys.pop(pop_key)
        self.currentCap += 1
        #place new node in list at the head (not used yet)
        self.insert_head(key, value)
        return      

    def insert_head(self, key, value):
        print("NEW HEAD")
        new_node = Node(key, value, self.head, self.head.nxt)
        self.head.nxt.prev = new_node
        self.head.nxt = new_node
        self.keys[key] = self.head.nxt


"""        
1 | 10
2 | 20
3 | 30

get 1 > head
get 3 >>> how to do it in O(1)??
---need to use a dictionary---
dictionary of pointers to the list?
"""