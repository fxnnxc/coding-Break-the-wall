


def solution(graph, a, b):
    count = -1
    

    retrun count






N = int(input())
a, b = map(int,input().split())
T = int(input())
graph ={}
for i in range(T):
    p, c =map(int, input().split())
    if p in graph.keys():
        graph[p].append(c)
    else:
        graph[p] = [c]

print(solution(graph,a,b))