




def solution(graph):
    cycles =[]
    dfs(graph)




N = int(input())
graph_temp = [list(map(int, input().split())) for i in range(N)]
graph = [[] for i in range(N)]

for i in range(N):
    for j in range(N):
        if graph_temp[j][i]==1:
            graph[i].append(j)


# cycles = solution(graph)
# print(len(cycles))
# print(cycles)
