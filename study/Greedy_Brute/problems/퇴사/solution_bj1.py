N = int(input())
lst = [list(map(int, input().strip().split())) for i in range(N)]

max_lst = [0 for i in range(N+1)]
for t in range(N):
    du, re = lst[t]
    if t+du<=N:
        max_lst[t+du] = max(max_lst[t+du], max(max_lst[:t+1])+re)
print(max(max_lst)) 