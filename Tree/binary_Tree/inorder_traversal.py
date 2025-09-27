# inorder Traversal 

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(root, newValue):

    if root is None:
        root = BinaryTreeNode(newValue)
        return root

    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)

    elif newValue > root.data:
        root.rightChild = insert(root.rightChild, newValue)

    return root 

def inorder(root):

    if root == None:return
    inorder(root.leftChild)
    print(root.data, end=' ')
    inorder(root.rightChild)

root= insert(None,15)
insert(root,10)
insert(root,25)
insert(root,6)
insert(root,14)
insert(root,20)
insert(root,60)


print('Inorder Traversal: ',end='')
inorder(root)