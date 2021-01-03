# 촌수계산


그래프의 두 노드의 거리를 구하는 문제


## Solution

```python
def solution(graph, a, b):
    global N
    visited=[0 for i in range(N+1)]
    length = [-1 for i in range(N+1)]
    queue = [a]
    length[a]=0
    while queue:
        t = queue.pop(0)
        visited[t] = True
        for i in graph[t]:
            if not visited[i]:
                queue.append(i)
                length[i]=length[t]+1
    return length[b]


N = int(input())
a, b = map(int,input().split())
T = int(input())
graph =[[] for i in range(N+1)]
for i in range(T):
    p, c =map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

print(solution(graph,a,b))
```
