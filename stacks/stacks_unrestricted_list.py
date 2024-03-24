class Stack:
    def __init__(self):
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
        
    def delete(self):
        self.list = None

    def push(self,value):
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
    

stack = Stack()
stack.push(1)
stack.push(20)
stack.push(30)

print(stack)

print(stack.isEmpty())

stack.pop()

print("-----")

print(stack)
print("-----")
print(stack.peek())


stack.delete()

print(stack)


