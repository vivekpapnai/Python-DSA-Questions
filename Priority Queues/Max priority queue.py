class priorityQueueNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        return False

    def getMax(self):
        return self.pq[0].value

    def __upHeapify(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = childIndex // 2
            if self.pq[childIndex].priority > self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
            else:
                break
            childIndex = parentIndex

    def insert(self, ele, priority):
        newNode = priorityQueueNode(ele, priority)
        self.pq.append(newNode)
        self.__upHeapify()

    def __downHeapify(self):
        parentIndex = 0
        leftChild = 2 * parentIndex + 1
        rightChild = 2 * parentIndex + 2
        while leftChild < self.getSize():
            getMax = parentIndex
            if self.pq[leftChild].priority > self.pq[getMax].priority:
                getMax = leftChild
            if rightChild < self.getSize() and self.pq[rightChild].priority > self.pq[getMax].priority:
                getMax = rightChild
            if getMax == parentIndex:
                break
            self.pq[getMax], self.pq[parentIndex] = self.pq[parentIndex], self.pq[getMax]
            parentIndex = getMax
            leftChild = 2 * parentIndex + 1
            rightChild = 2 * parentIndex + 2

    def removeMax(self):
        temp = self.pq[0].value
        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()
        self.__downHeapify()
        return temp


# Implement the removeMax() function here

myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1
