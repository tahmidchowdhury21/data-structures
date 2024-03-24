class Stack:
    def __init__(self,max_size=5):
        self.max_size = max_size
        self.list = []

    def  __str__(self):
        copy_values = self.list.copy()
        copy_values.reverse()
        copy_values = [str(x) for x in copy_values]
        return "\n".join(copy_values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        return len(self.list) == self.max_size
        
    def delete(self):
        self.list = None

    def push(self,value):
        if self.isFull():
            raise Exception("Stack is full")
        self.list.append(value)

    def pop(self):
        # print(self.list)
        if self.isEmpty():
            return "Empty Stack"
        popped =  self.list.pop()
        
        return popped

    def peek(self):
        if self.isEmpty():
            return "Empty Stack"
        return self.list[len(self.list) - 1]
    

stack = Stack(max_size=10)
stack.push(1)
stack.push(5)


print(stack)

print("-------")

print(stack.isFull())

