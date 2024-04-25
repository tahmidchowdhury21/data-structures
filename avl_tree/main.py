import sys
sys.path.append("../queues")
from queues_unrestricted_list import Queue

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        # LL_Rotation
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        # RR_Rotation
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        # LR_Rotation
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
         # RL_Rotation
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        # LL_Rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.rotate_right(root)
        # RR_Rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.rotate_left(root)
        # LR_Rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # L_Rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key < key:
            return self.search(root.right, key)

        return self.search(root.left, key)

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.key, end=" ")
            self.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        if root:
            print(root.key, end=" ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.key, end=" ")
    
    def levelOrderTraversal(self,rootNode):
        if rootNode is None:
            return
        else:
            custom_que = Queue()
            custom_que.enqueue(rootNode)

            while not custom_que.isEmpty():
                root = custom_que.dequeue()
                print(root.key,end="-")

                if root.left:
                    custom_que.enqueue(root.left)

                if root.right:
                    custom_que.enqueue(root.right)

# Example usage:
avl_tree = AVLTree()
avl_tree.root = avl_tree.insert(avl_tree.root, 10)
avl_tree.root = avl_tree.insert(avl_tree.root, 20)
avl_tree.root = avl_tree.insert(avl_tree.root, 30)
avl_tree.root = avl_tree.insert(avl_tree.root, 40)
avl_tree.root = avl_tree.insert(avl_tree.root, 50)
avl_tree.root = avl_tree.insert(avl_tree.root, 25)

print("Level order traversal:")
print(avl_tree.levelOrderTraversal(avl_tree.root))
print()

avl_tree.root = avl_tree.delete(avl_tree.root, 30)
print("\nAfter deletion of 30:")
print("\nLevel order traversal:")
print(avl_tree.levelOrderTraversal(avl_tree.root))
print()
