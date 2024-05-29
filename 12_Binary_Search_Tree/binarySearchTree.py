class Node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None

def createTree(a):
    root = None
    for value in a:
        root = insertNode(root, value)
    return root

# O(log N)
def insertNode(root, x):
    if root == None:
        return Node(x)

    if x < root.key:
        root.left = insertNode(root.left, x)
    elif x > root.key:
        root.right = insertNode(root.right, x)

    return root

# O(log N)
def searchNode(root, x):
    if root == None or root.key == x:
        return root

    if root.key < x:
        return searchNode(root.right, x)

    return searchNode(root.left, x)

# O(log N)
def searchUpperboundNode(root, x):
    if root == None:
        return root

    if root.key <= x:
        return searchUpperboundNode(root.right, x)

    upperBound = searchUpperboundNode(root.left, x)
    return upperBound if upperBound != None else root

# O(log N)
def searchLowerboundNode(root, x):
    if root == None:
        return root

    if root.key >= x:
        return searchLowerboundNode(root.left, x)

    lowerBound = searchLowerboundNode(root.right, x)
    return lowerBound if lowerBound != None else root

def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current

def deleteNode(root, x):
    if root == None:
        return root

    if x < root.key:
        root.left = deleteNode(root.left, x)
    elif x > root.key:
        root.right = deleteNode(root.right, x)
    else:
        if root.left == None:
            temp = root.right
            del root
            return temp
        if root.right == None:
            temp = root.right
            del root
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root

def loopTree(root):
    if root != None:
        loopTree(root.left)
        print(root.key, end=' ')
        loopTree(root.right)

def sizeTree(root):
    return 0 if root == None else sizeTree(root.left) + 1 + sizeTree(root.right)

def deleteTree(root):
    if root == None: return

    deleteTree(root.left)
    deleteTree(root.right)
    del root