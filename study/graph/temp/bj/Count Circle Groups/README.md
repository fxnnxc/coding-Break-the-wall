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
|solution4|failed|



## Solution
```python
import sys 

def solution(info):
    global N
    graph = [[] for i in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            x1,y1,r1 = info[i]
            x2,y2,r2 = info[j]
            if (x2-x1)**2 + (y2-y1)**2 <= (r1+r2)**2:
                graph[i].append(j)
                graph[j].append(i)
    count = 0
    visited = [False for i in range(N)]
    for i in range(N):
        if not visited[i]:
            count +=1
            visited[i] = True
            queue = [i]
            while queue:
                t = queue.pop()
                for j in graph[t]:
                    if not visited[j]:
                        visited[j]=True
                        queue.append(j)
    
    return count
    
T  = int(input())
for i in range(T):
    N = int(input())
    info = [list(map(int, sys.stdin.readline().split())) for j in range(N)]
    print(solution(info))

```
