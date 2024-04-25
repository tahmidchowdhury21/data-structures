import sys
sys.path.append("../queues")
from queues_unrestricted_list import Queue

class BSTNode:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

# Binary Search Tree is a type of Binary Tree
class BST:
    def __init__(self,value):
        self.bst_node = BSTNode(value)

    def insertNode(self, root_node, new_node_value):
        if root_node.value == None:
            self.bst_node = BSTNode(new_node_value)
        
        elif new_node_value <= root_node.value:
            if root_node.leftChild is None:
                root_node.leftChild = BSTNode(new_node_value)
            else:
                self.insertNode(root_node.leftChild, new_node_value)
        else:
            if root_node.rightChild is None:
                root_node.rightChild = BSTNode(new_node_value)
            else:
                self.insertNode(root_node.rightChild, new_node_value)
        return "Node was successfully inserted"
    
    def preOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        else:
            print(rootNode.value,end="-")
            self.preOrderTraversal(rootNode.leftChild)
            self.preOrderTraversal(rootNode.rightChild)

    def inOrderTraversal(self,rootNode):
        if rootNode is None:
            return
        else:
            self.inOrderTraversal(rootNode.leftChild)
            print(rootNode.value,end="-")
            self.inOrderTraversal(rootNode.rightChild)
    
    def postOrderTraversal(self,rootNode):
        if rootNode is None:
            return
        else:
            self.postOrderTraversal(rootNode.leftChild)
            self.postOrderTraversal(rootNode.rightChild)
            print(rootNode.value,end="-")

    def levelOrderTraversal(self,rootNode):
        if rootNode is None:
            return
        else:
            custom_que = Queue()
            custom_que.enqueue(rootNode)

            while not custom_que.isEmpty():
                root = custom_que.dequeue()
                print(root.value,end="-")

                if root.leftChild:
                    custom_que.enqueue(root.leftChild)

                if root.rightChild:
                    custom_que.enqueue(root.rightChild)
    
    def searhBST(self, root_node, value):
        if root_node.value == value:
            print("Value was found")
        
        elif value < root_node.value:
            if root_node.leftChild is not None:
                if root_node.leftChild.value == value:
                    print("Value was found")
                else:
                    self.searhBST(root_node.leftChild, value)
        else:
            if root_node.rightChild is not None:
                if root_node.rightChild.value == value:
                    print("Value was found")
                else:
                    self.searhBST(root_node.rightChild, value)
    
    def minNode(self, root_node):
        current = root_node
        while current.leftChild is not None:
            current = current.leftChild
        return current
    
    def delete_node(self, root_node, value):
        if root_node is None:
            return root_node
            
        if value < root_node.value:
            root_node.leftChild = self.delete_node(root_node.leftChild, value)
            
        elif value > root_node.value:
            root_node.rightChild = self.delete_node(root_node.rightChild, value)
            
        else:
            if root_node.leftChild is None:
                temp = root_node.rightChild
                root_node = None
                return temp

            if root_node.rightChild is None:
                temp = root_node.leftChild
                root_node = None
                return temp
                
            temp = self.minNode(root_node.rightChild)
            root_node.value = temp.value
            root_node.rightChild = self.delete_node(root_node.rightChild, temp.value)
            
        return root_node
    
    def delete_BST(self):
        self.bst_node.value = None
        self.bst_node.leftChild = None
        self.bst_node.rightChild = None
        print("Successfully deleted BST")

  



bst = BST(None)
bst.insertNode(bst.bst_node, 70)
bst.insertNode(bst.bst_node, 50)

bst.insertNode(bst.bst_node, 90)
bst.insertNode(bst.bst_node, 30)
bst.insertNode(bst.bst_node, 60)
bst.insertNode(bst.bst_node, 80)
bst.insertNode(bst.bst_node, 100)

bst.insertNode(bst.bst_node, 20)
bst.insertNode(bst.bst_node, 40)
# bst.insertNode(bst.bst_node, 95)
# bst.insertNode(bst.bst_node, 10)

# print(bst.bst_node.value)
# print(bst.bst_node.rightChild.value)

print("PreOrder: ")
bst.preOrderTraversal(bst.bst_node)

print("\n\nInOrder: ")
bst.inOrderTraversal(bst.bst_node)

print("\n\npostOrder: ")
bst.postOrderTraversal(bst.bst_node)

print("\n\nlevelOrder: ")
bst.levelOrderTraversal(bst.bst_node)

print("\n\n")
bst.searhBST(bst.bst_node,30)

bst.delete_node(bst.bst_node, 30)

print("\n\nlevelOrder: ")
bst.levelOrderTraversal(bst.bst_node)

bst.delete_BST()

print("\n\nlevelOrder: ")
bst.levelOrderTraversal(bst.bst_node)