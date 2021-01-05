# [바이러스](www.acmicpc.net/problem/2606)

## 문제
한 컴퓨터에 바이러스가 감염되면 연결되어 있는 모든 컴퓨터에 전파된다. 1번 컴퓨터가 바이러스에 감염되었다고 할 때, 1번 컴퓨터로 인해 감염된 컴퓨터의 개수를 출력한다.

## 입력
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
```
7
6
1 2
2 3
1 5
5 2
5 6
4 7
```
## 출력
```
4
```

## 코드
촌수계산 코드를 변형했다. bfs 사용
```
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list([0]*(n) for i in range(n))
visit = list([0]*(n))

def bfs(x):
    que = [x]
    while que:
        now = que.pop(0)
        for i in range(n):
            if arr[now][i] == 1 and visit[i] == 0:
                visit[i]=1
                que.append(i)

for i in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] = arr[y-1][x-1] = 1

bfs(0)

print(sum(visit)-1)
```
