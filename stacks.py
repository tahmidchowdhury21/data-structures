# LIFO Stack implementation using a Python list as
# its underlying storage.
class Stack:
    # Create an empty stack.
    def __init__(self):
        self.data = []

    # Add element e to the top of the stack
    def push(self, e):
        self.data.append(e)

    # Remove and return the element from the top of the stack
    # (i.e., LIFO). Raise exception if the stack is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data.pop()

    # Return (but do not remove) the element at the top of
    # the stack. Raise Empty exception if the stack is empty.
    def top_item(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data[-1]

    # Return True if the stack is empty.
    def is_empty(self):
        return len(self.data) == 0

    # Return the number of elements in the stack.
    def size(self):
        return len(self.data)


s = Stack()
s.push("S")
s.push("T")
s.push("A")
s.push("C")
s.push("K")
s.top_item()       # K
s.size()       # 5
s.is_empty()   # False
s.pop()        # K
s.pop()        # C
s.pop()        # A
s.pop()        # T
s.pop()        # s
s.is_empty()   # True
s.size()       # 0
s.top_item()       # IndexError: Stack is empty
