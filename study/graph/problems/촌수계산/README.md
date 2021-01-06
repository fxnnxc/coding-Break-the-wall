# 촌수계산

## [문제](https://www.acmicpc.net/problem/2644)

전체 사람의 수, 촌수를 계산하는 서로다른 두 사람의 번호, 관계의 개수, 부모 자식간의 관계를 나타내는 두 사람의 번호를 순서대로 입력할 때, 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력


```
INPUT
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

OUTPUT
3
```



## BFS
```
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = list([0]*(n) for i in range(n))
visit = list([0]*(n))

def bfs(x):
    que = [x]
    while que:
        now = que.pop(0)
        for i in range(n):
            if arr[now][i] == 1 and visit[i] == 0 :
                visit[i] = visit[now]+1
                que.append(i)

for i in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] = arr[y-1][x-1] = 1

bfs(a-1)

print(visit[b-1] if visit[b-1] else -1)
```

## DFS
```
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = list([0]*(n) for i in range(n))
num = int(0)
result = -1
def dfs(a, b, num, visit):
    visit.append(a)
    if a == b:
        global result
        result = num
        return

    for i in range(n):
        if arr[a][i] and i not in visit:
            dfs(i, b, num+1, visit)
    return

for i in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] = arr[y-1][x-1] = 1

dfs(a-1, b-1, 0, [])
print(result)
```
