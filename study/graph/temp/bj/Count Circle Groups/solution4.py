import sys 
# Queue Version

def solution(info):
    global N
    graph = {i:set([i]) for i in range(N)}
    for i in range(N):
        for j in range(i+1, N):
            x1,y1,r1 = info[i]
            x2,y2,r2 = info[j]
            if (x2-x1)**2 + (y2-y1)**2 <= (r1+r2)**2:
                graph[i].add(j)
                graph[j] = i

    values = [graph[i] for i in range(N)]
    return len(set(values))
    
T  = int(input())
for i in range(T):
    N = int(input())
    info = [list(map(int, sys.stdin.readline().split())) for j in range(N)]
    print(solution(info))