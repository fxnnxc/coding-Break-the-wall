# Count Circle Groups

## [문제](https://www.acmicpc.net/problem/10216)

![image](https://user-images.githubusercontent.com/52944973/103411487-98d11300-4bb3-11eb-95fe-e7e91a3caf9c.png)

Count Circle Groups

## 예제

![image](https://user-images.githubusercontent.com/52944973/103411497-ad151000-4bb3-11eb-8355-c9b04337480d.png)

## 문제 풀이 전략

처음 이 문제를 접했을때 2차원 map을 만들어서 bfs를 돌리면서 통신 영역을 표시하면서 영역이 겹치면 이어주는 형식으로 해결하려고 했으나 이렇게 해결할 경우 고려해야할 사항들이 너무 많다..

결국 오랜 고민 끝에 알고리즘을 참조 했는데, DFS를 활용한 Union-Find 문제였다.

알고리즘을 알고나니 5001 x 5001 배열을 만들어 줄 필요가 없었다.  
들어오는 순서대로 임의로 0번 노드 1번 노드 라고 생각하면 간단하다.

2차원 리스트를 만들고 0번 행은 0번 노드와 영역이 겹치는 노드들을 담는다. 그 다음 1번 행에는 1번 노드와 영역이 겹치는 노드들을 담는다. 이와 같이 N-1번 행까지 반복한다.

그리고 해당 노드를 방문한 적이 있는지를 나타내는 1차원 visited 배열을 만들어준다.

만들어진 배열을 가지고 DFS로 이어진 노드들의 visited 리스트 값을 True로 바꿔주면서 이어진 노드 그룹이 몇개인지 카운트해주면 끝이다.

## 코드

```python
def dfs(start):
    visited[start] = True
    for i in arr[start]:
        if visited[i]==False:
            dfs(i) 
    return 

T = int(input())
answer=[]

for _ in range(T):
    N=int(input())
    arr=[[] for _ in range(N)]
    distance=[]
    visited=[False for _ in range(N)]
    for _ in range(N):
        i,j,r=map(int,input().split())
        distance.append([i,j,r])
    for i in range(len(distance)-1):
        for j in range(i+1,len(distance)):
            if (distance[i][0]-distance[j][0])**2 +(distance[i][1]-distance[j][1])**2 <=(distance[i][2]+distance[j][2])**2:
                arr[i].append(j)
                arr[j].append(i)
    count = 0
    for i in range(N):
        if visited[i]== False:
            count+=1
            dfs(i)   
    answer.append(count)

for i in answer:
    print(i)
```
