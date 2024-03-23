from Node import DoubleNode
# Single Linkned List Class Definition
class DSLinkedList:
    def __init__(self,value=None):
        if value is not None:
            self.node = DoubleNode(value)

            self.head = self.node
            self.tail = self.node

            self.length = 1
        else:
            self.head = None
            self.tail = None

            self.length = 0
    
    def __str__(self):
        temp_node = self.head
        string = ' <- '
        if self.head is None:
            return f"Double LL is empty\nLength:  {self.length}"
        else:
            while temp_node:
                string += str(temp_node.value)
                if temp_node.next is not None:
                    string += " <-> "
                elif self.length ==1:
                    string += " <-> "
                temp_node = temp_node.next
        return f"{string}\nLength:  {self.length}"
            
            

    def append(self,value):
        new_node = DoubleNode(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

            self.tail = new_node

        self.length += 1

    def prepend(self,value):
        new_node = DoubleNode(value)

        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            
            self.head = new_node

        self.length += 1
    
    def traversal(self,reverse=False):
        temp_node = self.tail if reverse else self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.prev if reverse else temp_node.next
    
    def search(self,target):
        if self.length == 0:
            return False
        elif self.length == 1:
            return True if self.head.value == target else False
        else:
            temp_node = self.head
            while temp_node is not None:
                if temp_node.value == target:
                    return True
                temp_node = temp_node.next
        return False
    
    def get(self,index):
        if index >= self.length:
            # raise Exception("Index out of range")
            return None
        elif index == -1:
            temp_node = self.tail
        elif index < self.length // 2:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
        else:
            temp_node = self.tail
            for _ in range(self.length - 1, index, -1):
                temp_node = temp_node.prev
        return temp_node
    
    def set(self,index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        else:
            return False
        
    def insert(self,index,value):
        new_node = DoubleNode(value)
        temp_node = self.head

        if index == 0:
            if self.length == 0:
                self.head = self.tail = new_node
            elif self.length >= 1:
                new_node.next = temp_node
                
                temp_node.prev = new_node

                self.head = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next

            new_node.next = temp_node.next
            new_node.prev = temp_node

            temp_node.next = new_node
            temp_node.next.prev = new_node

        self.length += 1
    
dsl = DSLinkedList()
# dsl.append(5)
# dsl.append(10)
# print(dsl)
# dsl.prepend(34)

print(dsl)
# dsl.traversal(reverse=False)
# print(dsl.search(5))
# print(dsl.get(90).value)
# dsl.set(0,90)
# print(dsl)
dsl.insert(0,9999)
print(dsl)