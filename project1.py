class Node:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.parent = None
    
    def insertRequest(self, name, id):
        new_node = Node(name, id)
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
    
    def find_minimum(self, node):
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
        if id.left is None:
            self.transplant(id, id.right)
        elif id.right is None:
            self.transplant(id, id.left)
        elif id.right.left is None:
            self.transplant(id, id.right)
            id.right.parent = id.parent
            id.right.right = id.right
        else:
            tree_min = self.find_minimum(id.right)
            self.transplant(id, tree_min)
            tree_min.parent = id.parent
            tree_min.left = id.left
        
        

    def isEmptyBST(self):
        return self.root is None

    def sizeBST(self):
        if self.root is not None:
            return self.sizeBST(self.right) + self.sizeBST(self.left) + 1
        else:
            return 0

    #def printBST():

class MaxHeap:
    def __init__(self, priority, id):
        self.priority = priority
        self.id = id


