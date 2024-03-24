
"""
Circular Queue DS implemented with restricted size using list
First In First Out
"""

class CirularQueue:
    def __init__(self, max_size):
        self.list = [None] * max_size

        self.front = self.rear = -1

        self.max_size = max_size
    
    def isEmpty(self):
        return self.rear == -1 
    
    def __str__(self):
        return " -> ".join([str(v) for v in self.list])
    
    def isFull(self):
        return (self.rear + 1) % self.max_size == self.front
    

    def enqueue(self,value):
        if self.isFull():
            raise Exception("Queue is full")
        
        elif self.isEmpty():
            self.front += 1
            
        self.rear = (self.rear + 1) % self.max_size
        
        self.list[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        
        temp_item = self.list[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1

            self.list[self.front] = None
            self.list[self.rear] = None
        else:
            self.front = (self.front + 1) % self.max_size
            self.list[self.front - 1] = None
        return temp_item
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.list[self.front]
    
    def delete(self):
        self.list = [None] * self.max_size

        self.start = -1
        self.top = -1
    
circular_queue = CirularQueue(max_size=5)
circular_queue.enqueue(1)
circular_queue.enqueue(20)
circular_queue.enqueue(30)
circular_queue.enqueue(40)
circular_queue.enqueue(50)


print("Printing: ",circular_queue)

print("Returned Deque Item: ",circular_queue.dequeue())

print("Printing: ",circular_queue)

print("Peek: ",circular_queue.peek())

circular_queue.delete()

print("Printing: ",circular_queue)






