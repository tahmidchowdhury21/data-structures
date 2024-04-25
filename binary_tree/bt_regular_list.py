# This BinaryTree was implements using the using regular list characteristics

class BinaryTree:
    def __init__(self,size):
        self.customList = [None] * size
        self.last_used_index = 0
        self.max_size = size

    def insertNode(self,value):
        if self.last_used_index + 1 == self.max_size:
            return "BinaryTree is Full"
        self.customList[self.last_used_index + 1] = value

        self.last_used_index += 1
        return "Successfully added to BinaryTree"
    
    def searchtNode(self,value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return "Successfully found node"
        return "Failure to find node"
    
    def preOrderTraversal(self,index):
        if index > self.last_used_index:
            return
        else:
            print(self.customList[index],end="->")
            self.preOrderTraversal(index*2)
            self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self,index):
        if index > self.last_used_index:
            return
        else:
            self.inOrderTraversal(index*2)
            print(self.customList[index],end="->")
            self.inOrderTraversal(index*2 + 1)
    
    def postOrderTraversal(self,index):
        if index > self.last_used_index:
            return
        else:
            self.postOrderTraversal(index*2)
            self.postOrderTraversal(index*2 + 1)
            print(self.customList[index],end="->")


    def levelOrderTraversal(self,index):
        for i in range(index, self.last_used_index+1):
            print(self.customList[i],end="->")


    def deleteNode(self,value):
        for i in range(1, self.last_used_index+1):
            if value == self.customList[i]:
                self.customList[i] = self.customList[self.last_used_index]
                self.customList[self.last_used_index] = None

                self.last_used_index -= 1
                return "Successfully deleted the node"
        return "Failure to delete the node"
    
    def emptyBTree(self):
        self.customList = None
        self.last_used_index = 0
        return "Successfully emptied the BTree"


    

bt = BinaryTree(8)
bt.insertNode(1)
bt.insertNode(2)
bt.insertNode(3)
bt.insertNode(4)
bt.insertNode(5)
bt.insertNode(6)
bt.insertNode(7)

# print(bt.searchtNode(0))

# print("preOrderTraversal: ",end="")
# bt.preOrderTraversal(1)

# print()


# print("inOrderTraversal: ",end="")
# bt.inOrderTraversal(1)

# print()


# print("postOrderTraversal: ",end="")
# bt.postOrderTraversal(1)

# print()


# print("levelOrderTraversal: ",end="")
# bt.levelOrderTraversal(1)

print()

print(bt.deleteNode(5))


bt.levelOrderTraversal(1)

bt.emptyBTree()

bt.levelOrderTraversal(1)






    