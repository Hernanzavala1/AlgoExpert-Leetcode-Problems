class Node:
    def __init__(self, value, left = None, right = None):
        super().__init__()
        self.value = value 
        self.left = left
        self.right = right
def inorder(root):
    if( root is None):
        return None
    inorder(root.left)
    print(root.value)
    inorder(root.right)
    return None
def preorder(root):
    if root is None:
        return None
    print(root.value)
    preorder(root.left)
    preorder(root.right)
    return None

def postorder(root):
    result = []
    if(root is None):
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.value)

root = Node(23, Node(13, Node(10), Node(11)), Node(15, Node(22)) )
postorder(root)