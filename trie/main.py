# Implementation of Trie Data structure, which is a part of binary tree
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root_node = TrieNode()

    def insertString(self, word):
        current_node = self.root_node
        for i in word:
            ch = i
            node = current_node.children.get(ch)
            if node is None:
                node = TrieNode()
                current_node.children.update({ch: node})
            current_node = node
        current_node.endOfString = True
        print("Successfully inserted")

    def searchString(self, word):
        current_node = self.root_node
        for i in word:
            ch = i
            node = current_node.children.get(ch)
            if node is None:
                return False
            current_node = node
        
        if current_node.endOfString is True:
            return True
        else:
            return False
        
    def insertString(self, word):
        current_node = self.root_node
        for i in word:
            ch = i
            node = current_node.children.get(ch)
            if node is None:
                node = TrieNode()
                current_node.children.update({ch: node})
            current_node = node
        current_node.endOfString = True
        print("Successfully inserted")
        
    
    def deleteString(self,root, word, index):
        ch = word[index]
        currentNode = root.children.get(ch)
        canThisNodeBeDeleted = False

        if len(currentNode.children) > 1:
            self.deleteString(currentNode, word, index+1)
            return False
        
        if index == len(word) - 1:
            if len(currentNode.children) >= 1:
                currentNode.endOfString = False
                return False
            else:
                root.children.pop(ch)
                return True
        
        if currentNode.endOfString == True:
            self.deleteString(currentNode, word, index+1)
            return False

        canThisNodeBeDeleted = self.deleteString(currentNode, word, index+1)
        if canThisNodeBeDeleted == True:
            root.children.pop(ch)
            return True
        else:
            return False



    
newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
newTrie.deleteString(newTrie.root_node, "App", 0)
print(newTrie.searchString("App"))