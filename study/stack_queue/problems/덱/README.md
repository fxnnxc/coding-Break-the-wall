# 덱

## 문제
* [link](https://www.acmicpc.net/problem/10866)
* Deque를 구현하는 문제

### Tip

커맨드로 들어오는 string으로 함수를 바로 호출하는 방법
```python
v = getattr(obj:Object, cmd:str)(args) # 파라미터 존재
v = getattr(obj:Object, cmd:str)()     # 파라미터 없음
```


## Solution
```python
# operations 
"""
[1,2,3]

push front  [X, 1,2,3]
push back   [1,2,3 X]
pop front   1
pop back    3
size        3
empty       0
front       1
back        3
"""
class Deque():
    def __init__(self):
        self.buffer = []

    def push_front(self, x):
        self.buffer.insert(0, x)

    def push_back(self, x):
        self.buffer.append(x)

    def pop_front(self):
        if len(self.buffer)==0:
            return -1
        else:
            return(self.buffer.pop(0))

    def pop_back(self):
        if len(self.buffer)==0:
            return -1
        else:
            return(self.buffer.pop(-1))

    def size(self):
        return len(self.buffer)

    def empty(self):
        return 1 if self.size()==0 else 0
    
    def front(self):
        return self.buffer[0] if self.size()!=0 else -1

    def back(self):
        return self.buffer[-1] if self.size() !=0 else -1


import sys     
deque = Deque()
C = int(sys.stdin.readline())
for i in range(C):
    cmd = sys.stdin.readline().split()
    if len(cmd)==1:
        v = getattr(deque, cmd[0])()
        if v is not None:
            print(v)
    else:
        v = getattr(deque, cmd[0])(cmd[1])
        if v is not None:
            print(v)

```
