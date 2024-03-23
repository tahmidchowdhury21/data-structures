from Node import Node
# Single Linkned List Class Definition
class SLinkedList:
    def __init__(self,value=None):
        if value is not None:
            self.node = Node(value)

            self.head = self.node
            self.tail = self.node

            self.length = 1
        else:
            self.head = None
            self.tail = None

            self.length = 0
    
    # Add Node in the end of Linked List
    def append(self,value=None):
        if value is not None:
            new_node = Node(value)
            
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1
    
    # Printing the instance variables for debugging
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        if result == "":
            return f"Linked List is Empty"
        else:
            return f"Linked List: {result}\nLenght: {self.length}\n"
    
    # Add Node in the begining of Linked List
    def prepend(self,value=None):
        if value is not None:
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1
    
    # Insert at specific index
    def insert(self,index,value):
        new_node = Node(value)
        temp_node = self.head

        if index > self.length or index < 0:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = temp_node
            self.head = new_node
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    # Looping through the LL
    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
    
    # Try to find a value exist or not in LL
    def search(self,target):
        if self.head is None:
            print("Linked List is empty")
        else:
            current_node = self.head
            while current_node:
                if current_node.value == target:
                    print(f"The following {target} is indeed in the linked list")
                    return True
                current_node = current_node.next
            print(f"The following {target} doesn't exist in the linked list")
            return False
    
    # Get a specific node using index
    def get(self,given_index,return_value=True):
        current_node = self.head
        index=0
        if given_index == -1:
            if return_value is True:
                return self.tail.value
            else:
                return self.tail
        else:
            while current_node:
                if index == given_index:
                    if return_value is True:
                        return current_node.value
                    else:
                        return current_node
                index += 1
                current_node = current_node.next
        return None

    # Setting a specific node using index
    def set(self,given_index,value):
        specific_node = self.get(given_index,return_value=False)
        if specific_node is not None:
            specific_node.value = value

    # Removing first element from LL
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head, self.tail = None,None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    # Removing last element from LL
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            popped_node = None
        elif self.length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            
            self.tail = temp_node
            temp_node.next = None

        self.length -= 1
        return popped_node

    def remove(self,index):
        if index > self.length or index < 0:
            return None
        elif index == self.length -1:
            self.tail = self.pop()
        elif index == 0:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next = None
        else:
            get_specific_node = self.get(index-1,return_value=False)
            popped_node = get_specific_node.next
            
            get_specific_node.next = popped_node.next
            popped_node.next = None

        self.length -= 1
        return popped_node

    def clear_ll(self):
        self.head = self.tail = None
        self.length = 0


    def getfromLast(self,index):
        pointer_1 = self.head
        pointer_2 = self.head

        for _ in range(index):
            if pointer_2 is None:
                return None
            pointer_2 = pointer_2.next
            
        
        while pointer_2:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
        return pointer_1
    
    def sum_list(self,ll_1,ll_2):
        new_ll = SLinkedList(self)

        
        temp_head_1 = ll_1.head
        temp_head_2 = ll_2.head

        extra_number = 0
        while temp_head_1:
            both_nodes_added= str(temp_head_1.value + temp_head_2.value + extra_number)

            first_part = both_nodes_added[0:-1]
            second_part = both_nodes_added[-1]


            if first_part!= "":
                extra_number = int(first_part)
            new_ll.append(second_part)


            temp_head_1 = temp_head_1.next
            temp_head_2 = temp_head_2.next

            
        return new_ll
    
    
ll = SLinkedList()
ll.append(10)
ll.append(50)
ll.prepend(20)
# ll.insert(0,5)
# print(ll)
# ll.traverse()
# ll.search(9)

# print(ll.get(3))
# print("================================")
# ll.set(0,100)
# ll.traverse()

# print("================================")
# ll.pop_first()
# ll.traverse()
# print("================================")
# ll.pop()
# ll.pop()
# ll.pop()
# ll.pop()
# ll.traverse()
# print("================================")
# ll.append(10)
# ll.append(120)
# ll.append(130)
# ll.traverse()
# print("================================")
# ll.remove(20)
# ll.traverse()
# print("================================")
# ll.clear_ll()
# ll.traverse()
# print("================================")
# print(ll)
# print(ll.getfromLast(4).value)
ll_1 = SLinkedList()
ll_1.append(7)
ll_1.append(1)
ll_1.append(6)

ll_2 = SLinkedList()
ll_2.append(5)
ll_2.append(9)
ll_2.append(2)

print(ll.sum_list(ll_1,ll_2))

