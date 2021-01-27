# 센서
* [link](https://www.acmicpc.net/problem/2212)

## 풀이

센서의 개수 n개, 집중국의 개수 k 이므로 각 센서끼리의 거리 차를 구하고 큰 값을 가지는 차를 제외하고 나머지 거리에 대한 합계만 구하면 된다.


예를 들면 [1 6 9 3 6 7] 의 센서와 2개의 집중국이라 하자.

센서의 좌표를 오름차순으로 정렬해준다. [1 3 6 6 7 9]

센서의 좌표를 보면 3과 6에 위치한 두 센서가 가장 멀게 위치 하므로 [1 3] [6 6 7 9] 이렇게 나눠주는 게 효율적이다.

즉, 뒤에 위치한 센서와의 거리 차들을 구하고, 가장 거리의 차가 큰 값 k-1 개 제거 후, 나머지 차들의 합을 구하면 된다.

sub 이라는 배열에 센서 간 거리의 차를 넣는다. sub 배열 크기는 n-1 개가 된다.

sub = [2, 3, 0, 1, 2]

sub 배열을 오름차순으로 정렬한다.

sub = [0, 1, 2, 2, 3]

k-1 개 빼준 후 합계 출력

문제를 보면 n과 k가 될 수 있는 값의 범위가 일치하기 때문에
n보다 k가 크거나 같을 경우는 0을 출력함으로써 예외처리를 해준다. (안하면 index에러 남 ㅠㅠ)


## Solution
```
n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()
sub = []*(n-1)

if k>=n:
    print(0)
    exit()
    
for i in range(n-1):
    sub.append(arr[i+1]-arr[i])

sub.sort()

for i in range(k-1):
    sub.pop()

print(sum(sub))
```
