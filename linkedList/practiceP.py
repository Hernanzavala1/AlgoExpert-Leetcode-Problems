
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
def removeDuplicatesFromLinkedList(linkedList):
    seenVals = set()
    temp = linkedList
    prev = temp
    while(temp.next != None):
        if temp.value in seenVals:
            temp = temp.next
            prev = temp
        else:
            seenVals.add(temp.value)
            prev = temp 
            temp = temp.next
    return linkedList