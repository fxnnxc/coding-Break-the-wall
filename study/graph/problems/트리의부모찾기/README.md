# 트리의 부모 찾기
graph가 주어졌을 때, 한 노드를 root로 정하고 tree로 생각했을 때, 각 노드에 대한 부모 노드를 찾는 문제이다. 
* [link](https://www.acmicpc.net/problem/11725)

## 풀이

```python
# 세 개의 data structure를 사용한다. 
graph = [[] for i in range(N+1)]
parents = [-1 for i in range(N+1)]
visited = [False for i in range(N+1)]

# 부모 노드를 설정하는 방법
# (여기에 추가적으로 방문한 노드를 제외해주면 된다.)
queue = [1]
while queue:
    node = queue.pop()
    for neighbor in graph[node]:
        parents[neighbor] = node  # parent노드를 설정

```


## Solution
```python 
import sys 

N = int(input())
edges = [list(map(int, sys.stdin.readline().split())) for i in range(N-1)]
graph = [[] for i in range(N+1)]
for n1, n2 in edges:
    graph[n1].append(n2)
    graph[n2].append(n1)

parents = [-1 for i in range(N+1)]
visited = [False for i in range(N+1)]
queue = [1]
while queue: # BFS
    p = queue.pop()
    visited[p] = True 
    for nei in graph[p]:
        if not visited[nei]:
            queue.append(nei)
            parents[nei] = p

#print(parents)
for i in parents[2:]: # 첫 번째 제외
    print(i)
```