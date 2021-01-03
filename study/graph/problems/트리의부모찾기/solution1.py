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