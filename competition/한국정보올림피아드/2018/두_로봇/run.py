import sys

sys.setrecursionlimit(500000000)
N, r1, r2 = map(int, input().split())
cave_map = [[] for i in range(N + 1)]
visited = [0 for i in range(N + 1)]

for i in range(N - 1):
    c1, c2, l = map(int, input().split())
    cave_map[c1].append([c2, l])
    cave_map[c2].append([c1, l])


def dfs(r1, r2, s, m):
    #    print("재귀 진입")

    visited[r1] = 1

    if r1 == r2:
        print(s - m)
        exit(0)

    for i in cave_map[r1]:
        if visited[i[0]] == 0:
            dfs(i[0], r2, s + i[1], max(i[1], m))

    return


dfs(r1, r2, 0, 0)
