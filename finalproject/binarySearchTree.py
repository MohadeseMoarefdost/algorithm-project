class BSTNode:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.parent = None
    
    def insertRequest(self, id, name):
        new_node = BSTNode(id, name)
        y = None
        x = self.root
        while x is not None:
            y = x
            if new_node.id < x.id:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.id < y.id:
            y.left = new_node
        else:
            y.right = new_node
            
    def searchRequest(self, id):
        x = self.root
        while x is not None and id is not x.id:
            if id < x.id:
                x = x.left
            else:
                x = x.right
        return x
    
    def findMinimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def transplant(self, old, new):
        if old.parent is None:
            self.root = new
        elif old == old.parent.left:
            old.parent.left = new
        elif old == old.parent.right:
            old.parent.right = new
        if new is not None:
            new.parent = old.parent

    def deleteRequest(self, id):
        dNode = self.searchRequest(id)
        if dNode is None:
            return   
        if dNode.left is None:
            self.transplant(dNode, dNode.right)
        elif dNode.right is None:
            self.transplant(dNode, dNode.left)
        else:
            treeMinNode = self.findMinimum(dNode.right)
            if treeMinNode.parent != dNode:
                self.transplant(treeMinNode, treeMinNode.right)
                treeMinNode.right = dNode.right
                treeMinNode.right.parent = treeMinNode
            self.transplant(dNode, treeMinNode)
            treeMinNode.left = dNode.left
            treeMinNode.left.parent = treeMinNode

    def isEmptyBST(self):
        return self.root is None

    def sizeBST(self):
        def size(node):
            if node is None:
                return 0
            return size(node.left) + size(node.right) + 1
        return size(self.root)

    def preOrderTraversal(self, root):
        if root is None:
            return
        print(f'name: {root.name}   id: {root.id}')
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)      

    def printBST(self):
        self.preOrderTraversal(self.root)