class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class StackedLinkedList:
    def __init__(self,value=None):
        if value is None:
            self.head = self.tail = None
            self.length = 0
        else:
            self.new_node = Node(value)
            self.head = self.new_node
            self.tail = self.new_node
            self.length = 1

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
    
    def __str__(self):
        values = []
        temp_node = self.head
        while temp_node:
            values.append(temp_node.value)
            temp_node = temp_node.next
        return "\n".join(str(cv) for cv in values)
    
    def is_empty(self):
        return self.head is None
        
    
    def push(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def pop(self):
        if self.is_empty():
            return "Stacked LL is Empty"
        popped_node = self.head
        self.head = popped_node.next
        popped_node.next = None

        self.length -= 1

        return popped_node
    
    def peek(self):
        return "Stacked LL is Empty" if self.is_empty() else self.head.value
    
    def delete(self):
        self.head = self.tail = None
    

stacked_ll = StackedLinkedList()
stacked_ll.push(1)
stacked_ll.push(2)
stacked_ll.push(3)

print(stacked_ll)

print("---")

stacked_ll.pop()


print(stacked_ll)
print("---")

print(stacked_ll.peek())

print("------")
stacked_ll.delete()
print(stacked_ll)