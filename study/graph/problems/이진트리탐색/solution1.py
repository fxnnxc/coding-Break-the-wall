import sys 
sys.setrecursionlimit(100000)

class Node(object):
    def __init__(self, v, left=None, right=None):
        self.value = v
        self.left = left
        self.right = right
    
class Tree(object):
    def __init__(self, first_value):
        self.root = Node(first_value)

    def push(self, value): # O(logN) 
        """
        Find a parent node of the current value and make a new child node for the parent. 
        """
        parent = self.root 
        while True:         
            if value < parent.value:
                child = parent.left
            elif value > parent.value:
                child = parent.right
            if child is None : # No more travel
                break
            else:
                parent = child
        child = Node(value)
        if value < parent.value:
            parent.left = child
        elif value > parent.value:
            parent.right = child

    def postorder(self, node:Node): # L R N
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)

    def preorder(self):
        # N L R
        pass 

    def Inorder(self):
        # L N R 
        pass 

first_value = sys.stdin.readline()
tree = Tree(int(first_value))
while True:
    a = sys.stdin.readline()
    if a=="":
        break 
    else:
        tree.push(int(a))

tree.postorder(tree.root)

