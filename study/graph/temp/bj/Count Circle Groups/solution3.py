import sys 
# Queue Version

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