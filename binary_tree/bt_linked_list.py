import sys
sys.path.append("../queues")
from queues_unrestricted_list import Queue

# This BinaryTree was implements using the LinkedList characteristics

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,value):
        self.rootNode = Node(value)

    def printTree(self,traversal_type):
        if traversal_type == "in-order":
            print(f"in-order: {self.inOrderTraversal(self.rootNode,'')}")
        elif traversal_type == "pre-order":
            print(f"pre-order: {self.preOrderTraversal(self.rootNode,'')}")
        elif traversal_type == "post-order":
            print(f"post-order: {self.postOrderTraversal(self.rootNode,'')}")
        elif traversal_type == "level-order":
            print(f"level-order: {self.levelOrderTraversal(self.rootNode)}")
        else:
            print(f"{traversal_type} does not support yet")
            return False
    
    # Goes all the way to Left of the tree and if the last node is a leaf node(meaning no children)
    # Then print the last node, go up print the immediate parent node, and print that as well
    # Then do the same thing for the right current subtree
    
    # Then returen to root node and print, then
    
    # Repeat the whole thing on the right children of the root node, and this time don't come to root node
    def inOrderTraversal(self, rootNode, traversal):
        if rootNode is not None:
            traversal = self.inOrderTraversal(rootNode.left, traversal)
            traversal += str(rootNode.value) + " - "
            traversal = self.inOrderTraversal(rootNode.right, traversal)
        return traversal
    
    # Goes all the way to Left of the tree from root node and while doing so, its printing value of each node until it reaches last node and is a leaf node(meaning no children)
    # Then print the last node as well, then go to do the right side of the of the working parent node same way, 
    
    # Then do the same thing for the right root node
    
    def preOrderTraversal(self, rootNode, traversal):
        if rootNode is not None:
            traversal += str(rootNode.value) + " - "
            traversal = self.preOrderTraversal(rootNode.left, traversal)
            traversal = self.preOrderTraversal(rootNode.right, traversal)
        return traversal
    
    # Goes all the way to Left of the tree and while doing so, its printing value of each node ignorning root node until it reaches last node and is a leaf node(meaning no children)
    # Then print the last node as well, then go to do the right side of the of the working parent node same way, 
    
    # Then do the same thing for the right root node, finally come back to the root node
    
    def postOrderTraversal(self, rootNode, traversal):
        if rootNode is not None:
            traversal = self.postOrderTraversal(rootNode.left, traversal)
            traversal = self.postOrderTraversal(rootNode.right, traversal)
            traversal += str(rootNode.value) + " - "
        return traversal
    
    def levelOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        queue = Queue()
        queue.enqueue(rootNode)

        traversal = ""
        while not queue.isEmpty():
            traversal += str(queue.peek().value) + " - "
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal
    
    def checkIfValueExists(self, value, rootNode):
        if rootNode is None:
            return
        
        if rootNode.value == value:
            return True

        queue = Queue()
        queue.enqueue(rootNode)

        while not queue.isEmpty():
            node = queue.dequeue()

            if node.left:
                if node.left.value == value:
                    return True
                queue.enqueue(node.left)
            if node.right:
                if node.right.value == value:
                    return True
                queue.enqueue(node.right)

        return False


    def insertNode(self, new_node, rootNode):
        if rootNode is None:
            rootNode = new_node
        else:
            queue = Queue()
            queue.enqueue(rootNode)

            while not queue.isEmpty():
                node = queue.dequeue()

                if node.left is not None:
                    queue.enqueue(node.left)
                else:
                    node.left = new_node
                    return "Successfully added node "
                
                if node.right is not None:
                    queue.enqueue(node.right)
                else:
                    node.right = new_node
                    return "Successfully added node "
        
    def deleteBTree(self):
        self.rootNode.value = None
        self.rootNode.left = None
        self.rootNode.right = None
        return "Successfully deleted BTree "

        

binaryTree = BinaryTree(1)
binaryTree.rootNode.left = Node(2)
binaryTree.rootNode.right = Node(3)

binaryTree.rootNode.left.left = Node(4)
binaryTree.rootNode.left.right = Node(5)

binaryTree.rootNode.right.left = Node(6)
binaryTree.rootNode.right.right = Node(7)

binaryTree.printTree("in-order")
binaryTree.printTree("pre-order")
binaryTree.printTree("post-order")
binaryTree.printTree("level-order")

print(binaryTree.checkIfValueExists(8,binaryTree.rootNode))


print(binaryTree.insertNode(Node(8), binaryTree.rootNode))
binaryTree.printTree("level-order")

binaryTree.deleteBTree()

binaryTree.printTree("level-order")