class priorityQueueNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class priorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize() == 0

    def getMin(self):
        if self.getSize() == 0:
            return
        return self.pq[0].value

    def getValue(self):
        if self.isEmpty():
            return None
        return self.pq[0].value

    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, value, priority):
        pqNode = priorityQueueNode(value, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        parentIndex = 0
        leftChildren = 2*parentIndex + 1
        rightChildren = 2*parentIndex + 2
        while leftChildren < self.getSize():
            minIndex = parentIndex
            if self.pq[leftChildren].priority < self.pq[minIndex].priority:
                minIndex = leftChildren
            if rightChildren < self.getSize() and self.pq[rightChildren].priority < self.pq[minIndex].priority:
                minIndex = rightChildren
            if minIndex == parentIndex:
                # minIndex == parentIndex
                break
            self.pq[minIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[minIndex]
            parentIndex = minIndex
            leftChildren = 2 * parentIndex + 1
            rightChildren = 2 * parentIndex + 2

    def removeMin(self):
        if self.getSize() == 0:
            return
        temp = self.pq[0].value
        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()
        self.__percolateDown()
        return temp


myPq = priorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
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
