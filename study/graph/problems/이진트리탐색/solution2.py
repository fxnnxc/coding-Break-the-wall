import sys 

class Tree():
    def __init__(self, v):
        self.lst = [-1,v,0,0]
        self.size=len(self.lst)

    def push(self, v):
        parent = 0
        while True:
            if v < self.lst[parent]:
                child = parent*2
            elif v > self.lst[parent]:
                child = parent*2+1
            if self.lst[child]==0:
                break 
            else:
                parent=child
        if child*2+1>= self.size:
            self.lst = self.lst+[0 for i in range(self.size)]
            self.size = len(self.lst)
        if v < self.lst[parent]:
            self.lst[child] = v
        else:
            self.lst[child] = v

    def postorder(self, node): # L R N
        if node<=self.size and self.lst[node] !=0:
            self.postorder(node*2)
            self.postorder(node*2+1)
            print(self.lst[node])


first_value = sys.stdin.readline()
tree = Tree(int(first_value))
lst = []
while True:
    a = sys.stdin.readline()
    if a=="":
        break 
    else:
        tree.push(int(a))

tree.postorder(1)
