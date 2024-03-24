
"""
Queue  DS implemented with Linked Lists
First In First Out
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self,value=None):
        if value is None:
            self.head = self.tail = None

            self.length = 0
        else:
            self.new_node = Node(value)
            self.head = self.tail = self.new_node

            self.length = 1
    
    def isEmpty(self):
        return self.head is None
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
    
    def __str__(self):
        copy_list = [str(v.value) for v in self].copy()
        # copy_list.reverse()
        return " -> ".join([str(v) for v in copy_list])
    

    def enqueue(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            popped_node = self.head
            self.head = popped_node.next

        return popped_node
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.head
    
    def delete(self):
        self.head = self.tail = None

        self.length = 0
    
ll_queue = LinkedListQueue()
ll_queue.enqueue(1)
ll_queue.enqueue(20)
ll_queue.enqueue(30)
ll_queue.enqueue(40)
ll_queue.enqueue(50)



print("Printing: ",ll_queue)

print("Returned Deque Item: ",ll_queue.dequeue().value)

print("Printing: ",ll_queue)

print("Peek",ll_queue.peek().value)

print("Returned Deque Item: ",ll_queue.dequeue().value)
print("Returned Deque Item: ",ll_queue.dequeue().value)

print("Printing: ",ll_queue)

print("Peek",ll_queue.peek().value)

ll_queue.delete()

print("Printing: ",ll_queue)
