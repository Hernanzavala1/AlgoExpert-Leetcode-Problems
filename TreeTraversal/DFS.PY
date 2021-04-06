class Node:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.left = None
        self.right  = None
    def addChild(self, name):
        self.children.append(Node(name))
        return self
    def DFS(self, array): #iterative way
        #array is the result of letters
        stack = [self] # add  the root node to the stack
        while(len(stack) != 0):
            node = stack.pop() # get node and add children to the stack'
            if node.name in array:
                continue
            array.append(node.name)
            for child in node.children:
                stack.append(child)
        return array

    def DFS2(self, array):
        array.append(self.name)
        for child in self.children:
            child.DFS2(array)
        return array
root = Node("A")
root.addChild("B")
root.addChild("C")
root.addChild("D")
print(root.DFS([]))
