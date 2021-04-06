class Node:
    def __init__(self, value, left =None, Right = None):
        super().__init__()
        self.value = value
        self.left =left
        self.right = Right

class BST:
    def __init__(self):
        super().__init__()
        self.root = None


    def insert(self, value):
        if(self.root == None):
            self.root = Node(value)
            return None
        currentNode = self.root
        prev = currentNode
        while(currentNode != None ):
            prev = currentNode
            if(value < currentNode.value):
                currentNode = currentNode.left
            elif(value > currentNode.value):
                currentNode = currentNode.right
            else:
                print("already in the tree")
                return None
        if(value < prev.value):
            prev.left =  Node(value)
        else:
            prev.right = Node(value)
    def insert_rec(self,value, root):
        if(root == None):
            return Node(value)
        if(value < root.value ):
            root.left = self.insert_rec(value , root.left)
        else:
            root.right = self.insert_rec(value, root.right)
        return root
            
    def print_Tree(self, node):
        #this is inorder traversal
        if(node.left != None):
            self.print_Tree(node.left)
        print(node.value)
        if(node.right != None):
            self.print_Tree(node.right)
    def findClosestValueInBst(self, node, target):
    # Write your code here.
        currentClosest = [] # the first index will be the difference and the second will be the actual number
        currentNode  = node
        while(currentNode != None):
            if(currentNode.left != None and currentNode.right != None ):
                left = abs(target - currentNode.left.value)
                right = abs(target - currentNode.right.value)
                if(left < right ):
                    currentClosest[0] = left
                    currentClosest[1] = currentNode.left.value
                    currentNode = currentNode.left
                else:
                    currentClosest[0] = right
                    currentClosest[1] = currentNode.right.value
                    currentNode = currentNode.right
    def closest(self, root, target):
        currentClosest = {"difference": 10000000, "value" :-1}
        currentNode = root
        while(currentNode != None):
            if(target >= currentNode.value):
                newMin = abs(target - currentNode.value)
                if(newMin < currentClosest['difference']):
                    currentClosest["difference"] = abs(target - currentNode.value)
                    currentClosest["value"] = currentNode.value
                currentNode = currentNode.right
            else:
                newMin = abs(target - currentNode.value)
                if(newMin < currentClosest['difference']):
                    currentClosest["difference"] = abs(target - currentNode.value)
                    currentClosest["value"] = currentNode.value
                currentNode = currentNode.left
        return currentClosest["value"]
    
    def branchSum(self, root):
        if(root ==  None):
            return []
        if(root.left == None and root.right == None):
            # return root.value
            return [root.value]
        leftSum = branchSum(root.left) # for each of the elements in the array add the root value 
        if(leftSum != []):
            for index in range(len(leftSum)):
                leftSum[index] += root.value
        rightSum = branchSum(root.right)
        if(rightSum != []):
            for index in range(len(rightSum)):
                rightSum[index] += root.value
        result = leftSum + rightSum
        return result
        

        
# tree = BST()
# tree.root = tree.insert_rec(10, tree.root)
# tree.root = tree.insert_rec(5, tree.root)
# tree.root = tree.insert_rec(15, tree.root)
# tree.root = tree.insert_rec(2, tree.root)
# tree.root = tree.insert_rec(5, tree.root)
# tree.root = tree.insert_rec(13, tree.root)
# tree.root = tree.insert_rec(22, tree.root)
# tree.root = tree.insert_rec(1, tree.root)
# tree.root = tree.insert_rec(14, tree.root)
# print(tree.closest(tree.root, 12))
