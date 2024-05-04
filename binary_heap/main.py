class BinaryHeap:
    # Initialize binary heap with maxSize
    def __init__(self, maxSize):
        self.customList = (maxSize + 1) * [None]  # Custom list to store heap elements
        self.currentHeapSize = 0  # Current size of the heap
        self.maxSize = maxSize  # Maximum size of the heap
    
    # Return the root of the heap
    def peek(self):
        if self.currentHeapSize == 0:
            return -1  # Indicate empty heap
        return self.customList[1]
    
    # Return current size of the heap
    def sizeOfHeap(self):
        if self.currentHeapSize == 0:
            return 0
        return self.currentHeapSize
    
    # Print heap elements in level order traversal
    def levelOrderTraversal(self):
        if self.currentHeapSize == 0:
            return "Binary heap is empty"
        else:
            for i in range(1,self.currentHeapSize + 1):
                print(self.customList[i])

    # Helper function to maintain heap property during insertion
    def heapifyTreeInsert(self, customList, index, heapType):
        parentIndex = int(index/2)
        if index <= 1:
            return
        
        if heapType == "Min":
            if customList[index] < customList[parentIndex]:
                temp = customList[index]
                customList[index] = customList[parentIndex]
                customList[parentIndex] = temp
            self.heapifyTreeInsert(customList, parentIndex, heapType)
        
        elif heapType == "Max":
            if customList[index] > customList[parentIndex]:
                temp = customList[index]
                customList[index] = customList[parentIndex]
                customList[parentIndex] = temp
            self.heapifyTreeInsert(customList, parentIndex, heapType)

    # Insert a node into the heap
    def inserNode(self, nodeValue, heapType):
        if self.currentHeapSize + 1 == self.maxSize:
            return "Binary heap is full"
        self.customList[self.currentHeapSize + 1] = nodeValue
        self.currentHeapSize += 1
        self.heapifyTreeInsert(self.customList, self.currentHeapSize, heapType)

    # Helper function to maintain heap property during extraction
    def heapifyTreeExtract(self, customList, index, heapType):
        leftIndex = index * 2
        rightIndex = index * 2 + 1
        swapChild = 0

        if self.currentHeapSize < leftIndex:
            return
        elif self.currentHeapSize == leftIndex:
            if heapType == "Min":
                if customList[index] > customList[leftIndex]:
                    temp = customList[index]
                    customList[index] = customList[leftIndex]
                    customList[leftIndex] = temp
                return
            else:
                if customList[index] < customList[leftIndex]:
                    temp = customList[index]
                    customList[index] = customList[leftIndex]
                    customList[leftIndex] = temp
                return
        else:
            if heapType == "Min":
                if customList[leftIndex] < customList[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if customList[index] > customList[swapChild]:
                    temp = customList[index]
                    customList[index] = customList[swapChild]
                    customList[swapChild] = temp
            else:
                if customList[leftIndex] > customList[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if customList[index] < customList[swapChild]:
                    temp = customList[index]
                    customList[index] = customList[swapChild]
                    customList[swapChild] = temp
            self.heapifyTreeExtract(customList, swapChild, heapType)

    # Extract the root node from the heap
    def extractNode(self, heapType):
        if self.currentHeapSize == 0:
            return None
        else:
            extracted_node = self.customList[1]  # Root of the heap
            self.customList[1] = self.customList[self.currentHeapSize]  # Move last element to root
            self.customList[self.currentHeapSize] = None  # Remove last element
            self.currentHeapSize -= 1  # Decrease heap size
            self.heapifyTreeExtract(self.customList, 1, heapType)
            return extracted_node

# Example usage
binaryHeap = BinaryHeap(5)
print(binaryHeap.peek())
print(binaryHeap.sizeOfHeap())
binaryHeap.levelOrderTraversal()

print("--------------------------")

binaryHeap.inserNode(4, "Max")
binaryHeap.inserNode(5, "Max")
binaryHeap.inserNode(2, "Max")
binaryHeap.inserNode(1, "Max")

binaryHeap.levelOrderTraversal()

print("--------------------------")

binaryHeap.extractNode("Max")
binaryHeap.levelOrderTraversal()
