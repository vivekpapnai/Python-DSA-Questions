class mapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class hashMap:
    def __init__(self):
        self.bucketSize = 20
        self.bucket = []
        self.count = 0

    def size(self):
        return self.count

    def isPresent(self, key):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                return True
            head = head.next
        return False

    def getValue(self, key):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return False

    def removeKey(self, key):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.bucket[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.bucket[index] = head.next
                else:
                    prev.next = head.next
                self.count -= 1
                return True
            prev = head
            head = head.next
        return False

    def getIndex(self, hc):
        return abs(hc) % self.bucketSize

    def rehash(self):
        temp = self.bucket
        self.bucketSize = self.bucketSize * 2
        self.bucket = [None for i in range(self.bucketSize)]
        self.count = 0
        for head in temp:
            while head is not None:
                self.insert(head.key, head.value)
                head = head.next

    def insert(self, key, value):
        hc = hash(key)
        index = self.getIndex(hc)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                head.value = value
            head = head.next
        head = self.bucket[index]
        newNode = mapNode(key, value)
        newNode.next = head
        self.bucket[index] = newNode
        self.count += 1
        if self.count / self.bucketSize >= 0.7:
            self.rehash()


def largestSubSeq(n, arr):
    mp = hashMap()
    start = 0
    maxLen = 0
    for i in arr:
        mp.insert(i, 'T')
    for i in range(n):
        if mp.getValue(i)=="T":
            pass


n = int(input())
arr = [int(x) for x in input().split()]
largestSubSeq(n, arr)
