# The Great Revegetation



## 문제 

```
input
3 2
S 1 2
D 3 2

output
10

```

## 풀이
```
N = 농작지의 길이
M = 소의 마리 수 
ㅁㅁㅁ 세 칸이 있을 때, 
첫 번째 소는 1 2 칸에 똑같은 타입의 작물을 심어야 한다. 
두 번째 소는 3,2 칸에 다른 작물을 심어야 한다. 

A A B
B B A
2 -> 이진수 -> 10 
```


## Solutions

|Solution|info|
|:-:|:-:|
|[solution1.py](solution1.py)|unsloved, timeout|
|[solution2.py](solution2.py)|unsloved, timeout|
|[solution3.py](solution3.py)|unsloved, type이 같은 애들끼리 묶음. timeout|
|[solution4.py](solution4.py)|unsloved, type이 같은 애들끼리 비교를 빠르게 함.  timeout|


## solution
```python

# Time out!!!
import sys 
sys.setrecursionlimit(100000)
count = 0

def evaluate(lst, diff_graph, match):
    global N
    for i,j in diff_graph:
        if lst[match[i]]==lst[match[j]]:
            return False
    return True

def generate(lst, K, diff_graph, match):
    global count
    if evaluate(lst, diff_graph, match):
        if len(lst)==K:
                count +=1
        else:
            for i in ['A', 'B']:
                lst.append(i)
                generate(lst, K, diff_graph, match)
                lst.pop()

def solution(info):
    global N, M
    diff_info = []
    components  = [i for i in range(N)]
    for i in range(M):
        food_type, g1,g2 = info[i]
        if food_type=="S":
            small, large = min(g1, g2), max(g1, g2)
            components[large] = components[small]
        else:
            diff_info.append([components[g1], components[g2]])

    sets = [[] for i in range(N)]
    for i in range(N):
        sets[components[i]].append(i)

    match = {i:i for i in range(N)}
    cur = -1
    for i,s in enumerate(sets):
        if len(s)==0:
            cur -=1
        cur +=1
        match[i] = cur

    generate([], len([s for s in sets if s]), diff_info, match)


N, M = map(int, input().split())
info = list(map(lambda x:(x[0], int(x[1])-1, int(x[2])-1), [sys.stdin.readline().strip().split() for i in range(M)]))
solution(info)
print(f"{count:b}", end="")

```
