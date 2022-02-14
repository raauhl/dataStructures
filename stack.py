class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        data = Node(data, None)
        data.next = self.top
        self.top = data
    
    def pop(self):
        item = self.top
        if item is not None:
            self.top = self.top.next
        return item
    
    def top(self):
        return self.top