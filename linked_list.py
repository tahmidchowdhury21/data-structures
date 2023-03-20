class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def add_data_to_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None

    def add_to_middle(self, data, position):
        if position == 1:
            self.add_data_to_begin(data)
            return
        new_node = Node(data)
        current_node = self.head
        count = 1
        while current_node is not None and count < position:
            previous_node = current_node
            current_node = current_node.next
            count += 1
        if current_node is None and count != position:
            print(
                f"Invalid position {position} for a linked list of length {count-1}")
            return
        previous_node.next = new_node
        new_node.next = current_node

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


ls = LinkedList()
ls.add_to_end(1)
ls.add_to_end(2)
ls.add_to_end(3)
ls.print_list()
print()
ls.add_data_to_begin(0)
ls.print_list()
print()
ls.add_to_middle(44, 2)
ls.print_list()
ls.remove_from_end()
ls.print_list()
