class Stack:
    def __init__(self):
        self.name = []

    def empty(self):
        if len(self.name) == 0:
            return True
        else:
            return False
    
    def push(self, data):
        self.name.append(data)
        return self.name
        
    def top(self):
        if len(self.name) == 0:
            return None
        return self.name[-1]

    def pop(self):
        
        if len(self.name) == 0:
            return None
        else:
            return self.name.pop(-1)
        
    def __repr__(self):
        return self.name


# instance = Stack()
# instance2 = Stack() 
# instance.push(1)
# instance.push(2)
# instance.push(3)
# instance.push(4)
# instance.push('a')
# instance.push('b')

# instance2.push(3)
# instance2.push(4)
# instance2.push('a')


# print(instance.empty())
# print(instance.top())
# print(instance.pop())
# print(instance.__repr__())

# print(instance2.empty())
# print(instance2.top())
# print(instance2.pop())
# print(instance2.__repr__())