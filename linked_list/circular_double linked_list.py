from Node import DoubleNode
# Single Linkned List Class Definition
class CDLinkedList:
    def __init__(self,value=None):
        if value is not None:
            self.node = DoubleNode(value)

            self.head = self.node
            self.tail = self.node

            self.tail.next = self.node

            self.length = 1
        else:
            self.head = None
            self.tail = None

            self.length = 0
    
    def __str__(self):
        temp_node = self.head
        string = ' <- '
        if self.head is None:
            return f"Circular Double LL is empty\nLength:  {self.length}"
        else:
            while temp_node:
                string += str(temp_node.value)
                if temp_node.next is not None:
                    string += " <-> "
                elif self.length ==1:
                    string += " <-> "
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break
        return f"{string}\nLength:  {self.length}"
    
    def prepend(self,value):
        new_node = DoubleNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node

            self.head = new_node

            self.tail.next = self.head

        self.length += 1
    
    def append(self, value):
        new_node = DoubleNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

            self.tail.next = new_node
        else:
            self.tail.next = new_node

            new_node.prev = self.tail

            self.tail = new_node

            new_node.next = self.head
        
        self.length += 1

    def insert(self, index, value):
        new_node = DoubleNode(value)
        if self.head is None:
            print("DC LL is Empty")
            return
        else:
            if index == -1 or index == self.length:
                self.append(new_node)
            else:
                temp_node = self.head
                for _ in range(index-1):
                    temp_node = temp_node.next
                
                new_node.next = temp_node.next
                temp_node.next = new_node
                new_node.prev = temp_node

                temp_node.next.prev = new_node
            
        self.length += 1


            
            

cdll = CDLinkedList(1)
# cdll.prepend(1)
# cdll.prepend(0)
# cdll.append(5)
# cdll.append(7)
print(cdll)

cdll.insert(2,55)
print(cdll)

