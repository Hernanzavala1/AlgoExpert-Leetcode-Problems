class Node:
    def __init__(self, num,  next = None):
        self.num = num
        self.next = next

class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
    # this method will be inserting at the head
    def insert(self,number):
        newNode = Node(number, self.head)
        self.head = newNode
    # this method prints in the forward direction
    def traverse(self, node):
        if(node == None):
            return None
        print(node.num)
        self.traverse(node.next)
    # This method prints in the backwards direction
    def traverse2(self, node):
        if(node == None):
            return None
        self.traverse(node.next)
        print(node.num) # This will start executing after the last node was visited. Which is why it starts printing backwards
    def searchNode(self, position):
        # the head will be at position 0, and we will count up from there\
        if(self.head == None):
            return None
        count = 0
        node = self.head
        while(node != None):
            if(count == position):
                return node
            count+= 1
            node= node.next
        return None
    def valueExist(self, val, node):
        if(node == None):
            return "false"
        if(node.num == val):
            return "True"
        return self.valueExist(val,node.next)
    def sortInsert(self, val):
        newNode = Node(val) #initialize the new node
        if(self.head == None):
            self.head = newNode
            return None
        if (self.head.num >= val):
            newNode.next = self.head
            self.head = newNode
            return None
        prev = self.head
        current = self.head
        while(current != None):
            if(current.num >= val):
                newNode.next = current
                prev.next = newNode
                return None
            else:
                prev = current
                current = current.next
        prev.next = newNode
        return None
    def reverseListR(self, node):
        if(node == None):
            return node
        if(node.next == None):
            return node
        
        node1 = reverseListR(node.next)
        next = node.next
        next.next = node
        node.next = None
        return node1
    def removeDup(self, head):
        nums = set() # keep track of numbers already seen
        prev = head
        result = head
        while(head.next != None):
            if(head.num not in nums):
                nums.add(head.num)
            else:
                #remove this number because it is a duplicate
                prev.next = head.next #skip over the current node
            prev, head  = head, head.next
        return result
    def KthElem(self, k):
        pass
    def deleteMiddleNode(self, Node):
        # copy the info from the next and then skip over it
        if(Node.next == None):
            return None
        Node.num = Node.next.num
        Node.next = Node.next.next

    def partitionList(self, val):
        pass
        
li = LinkedList()
li.insert(1)
li.insert(2)
li.insert(1)
li.insert(3)
head = li.removeDup(li.head)
li.traverse(head)