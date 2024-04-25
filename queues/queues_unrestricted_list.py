
"""
Queue DS implemented with unrestricted size normal list
First In First Out
"""

class Queue:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        if self.list == [] or self.list == None:
            return 'Queue is empty'
        return " -> ".join([str(v) for v in self.list])
    
    def isEmpty(self):
        return self.list == []
    
    def enqueue(self,value):
        self.list.append(value)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.list.pop(0)
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.list[0]
    
    def delete(self):
        self.list = None

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue)

    print("-------")

    queue.dequeue()

    print(queue)

    print("-------")

    queue.delete()

    print(queue)