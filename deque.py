class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def push_front(self, data):
        node = Node(data)

        if self.front is None:
            self.front = self.rear = node
            return
        
        node.next = self.front
        self.front.prev = node
        self.front = node

    def push_rear(self, data):
        node = Node(data)

        if self.rear is None:
            self.front = self.rear = node
            return
        
        node.prev = self.rear
        self.rear.next = node
        self.rear = node

    def pop_front(self):
        item = self.front
        
        if item is None:
            return item
        
        if item.next is None:
            self.front = self.rear = None
            return item
        
        item.next.prev = None
        self.front = item.next
        return item

    def pop_rear(self):
        item = self.rear
            
        if item is None:
            return item
        
        if item.prev is None:
            self.front = self.rear = None
            return item
        
        item.prev.next = None
        self.rear = item.prev
        return item
    
    def show_front(self):
        return self.front

    def show_rear(self):
        return self.rear

