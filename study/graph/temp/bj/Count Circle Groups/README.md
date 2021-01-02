# Count Circle Groups


## 풀이

N개의 위치에 대해서 먼저 각각을 그룹으로 생각한다. 
첫 번째 위치에 대해서 그룹을 이루는 얘들을 모두 모은다. GROUP1
두 번째 위치에 대해서 세 번째부터 그룹을 이루는 얘들을 모은다. 
...
N-1 번째와 N이 그룹을 이루는지 확인한다. 


혹은

관계성에 대해서 graph를 그리고 connected component를 찾는다. 
점에서 탐험

|Solutions| info|
|---|---|
|solution1|base|
|solution2|base+sys.stdin|
|solution3|queue version|


## Solution
```python
import sys 
sys.setrecursionlimit(100000)

count = 0

# S -> i, j 이면 두 edge는 연결되어 있다. N개
# graph에서 연결된 애들끼리 묶는다.  P 개 집합
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
