class Stack:
    def __init__(self):
        self.items = []

    def s_Stack(self):
        return self.items
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()


stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print( stack1.s_Stack() )

stack1.pop()
print( stack1.s_Stack() )


