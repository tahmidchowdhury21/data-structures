from Node import Node

# Curcular Single Linkned List Class Definition
class CSLinkedList:
    def __init__(self,value=None):
        if value is not None:
            self.node = Node(value)

            self.head = self.node
            self.tail = self.node

            self.tail.next = self.node

            self.length = 1
        else:
            self.head = None
            self.tail = None

            self.length = 0
    
    # Add Node in the end of Linked List
    def append(self,value=None):
        if value is not None:
            new_node = Node(value)
            
            if self.length == 0:
                self.head = new_node
                self.tail = new_node

                new_node.next = self.head

            else:
                self.tail.next = new_node
                new_node.next = self.head
                self.tail = new_node

            self.length += 1
    
    # Printing the instance variables for debugging
    def __str__(self):
        if self.head is  None:
            return f"Linked List is Empty"
        temp_node = self.head
        result = ""
        while temp_node.next is not None:
            result += str(temp_node.value)
            # if temp_node.next is not None:
            #     result += " -> "
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " -> "
        if result == "":
            return f"Linked List is Empty"
        else:
            return f"Linked List: {result}\nLenght: {self.length}\n"
    
    def prepend(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node

            self.tail.next = self.head

        self.length += 1

    def insert(self,index,value):
        new_node = Node(value)
        if index < -1 or index > self.length:
            raise Exception(f"Index out of bounds {index} must be between 0 and {self.length}")
        elif index == 0:
            if self.length == 0:
                self.head = self.tail = new_node
                self.tail.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node

                self.tail.next = self.head
        elif index == -1 or index == self.length:
            self.tail.next = new_node
            self.tail = new_node

            new_node.next = self.head
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        
        self.length += 1

    def traversal(self):
        temp_node = self.head
        if self.length == 0:
            print("CLL is empty")
        else:
            while temp_node is not None:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.head:
                    break
    
    def search(self,value):
        temp_node = self.head
        current_index = 0
        if self.length == 0:
            print(f"Value does not exist in the CSLL LLL")
            return False
        else:
            while temp_node is not None:
                if temp_node.value == value:
                    print(f"Value {value} exists in index %d" % current_index)
                    return True
                current_index += 1
                temp_node = temp_node.next
                if temp_node == self.head:
                        break
        print(f"Value does not exist in the CSLL")
        return False
    
    def get(self,index, get_node=False):
        temp_node = self.head
        if index > self.length or index < -1:
            raise Exception("Index out of range")
        elif index == -1:
                return self.tail.value if get_node is False else self.tail
        elif index == 0:
            return temp_node.value if get_node is False else temp_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            return temp_node.next.value if get_node is False else temp_node
    
    def set(self,index,value):
        specific_node = self.get(index, get_node=True)
        if index == 0 and self.length !=0:
            self.head.value = value
        else:
            specific_node.next.value = value
    
    def pop_first(self):
        deleted_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = self.tail = None
        else:
            self.head = deleted_node.next
            self.tail.next = deleted_node.next

            deleted_node.next = None

        self.length -= 1
        return deleted_node
    
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not popped_node:
                temp_node = temp_node.next
            
            self.tail = temp_node
            temp_node.next = self.head

            popped_node.next = None

        self.length -= 1
        return popped_node
    
    def remove(self,index):
        temp_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1 or index == 0:
            popped_node = self.pop_first()
        elif index == -1 or index == self.length:
            popped_node = self.pop()
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            
            popped_node = temp_node.next
            temp_node.next = popped_node.next

            popped_node.next = None

            self.length -= 1
        return popped_node
    
    def removeAll(self):
        self.tail.next = None
        self.head = self.tail = None
        self.length = 0

        
        

    
cll = CSLinkedList()
cll.append(2)
cll.append(23)
cll.append(24)

# cll.prepend(1)
# cll.prepend(0)
# cll.insert(0,5)


# cll.traversal()
# cll.search(89)
# print(cll)
# print(cll.get(0,get_node=True))
# cll.set(2,500)
# print(cll)
# print(cll.pop_first())
# print(cll)
# cll.remove(1)
print(cll)
cll.removeAll()
print(cll)
