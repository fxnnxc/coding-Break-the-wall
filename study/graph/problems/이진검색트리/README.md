# 이진 검색 트리


## [문제](https://www.acmicpc.net/problem/5639)

트리 정보에 대한 전위 순회 결과가 주어질 때, 후위 순위 정보를 찾는 문제. 


```
50 30 24 5 28 45 98 52 60
50 30  24 | 5 | 28 45 98 52 60
50 | 30 | 24 ` 0 ` 28 45 98 52 60
왼쪽 오른쪽 가운데를 Recursive하게 나누고 [A B~~~  C~~~] 출력  

출력
5 28 24 45 30 60 52 98 50
```


## Solutions
|solution|time|info|
|:-:|:-:|:-:|
|[solution1.py](solution1.py)|880ms|python3는 시간초과가 난다. |
|[solution2.py](solution2.py)|X|tree의 리스트 버전, 시간 초과가 난다. |


```python
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

```