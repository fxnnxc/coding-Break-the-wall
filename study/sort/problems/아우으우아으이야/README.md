# 아우으 우아으이야!!

## [문제](https://www.acmicpc.net/problem/15922)

퇴사를 진행행하려 하는는데 N+1일 째 되는날 퇴사를 하기 위해서 N일 동안 많은 상담을 하려고 한다.

상담을 완료하는데 걸리는 시간 T와 상담을 했을 때 받을 수 있는 금액 P를 보고, 퇴사 전까지 최대 수익을 구하는 문제이다.

## 예제

```
입력
5
-5 -2
-3 0
2 5
6 10
8 12

출력
14

```

## 문제 풀이 전략

## Results

|            Version             | Memory  | Time(ms) | info     |
| :----------------------------: | :-----: | :------: | :------- |
| solution1.py([solution_ji.py]) | 48500KB |  4048ms  | Baseline |

## Solution 1

```python
N = int(input())#N개의 선분
lines = []
for _ in range(N):
    lines.append(list(map(int,input().split())))

pre_s, pre_e = lines[0][0],lines[0][1]
length = pre_e-pre_s

for i in range(1,N):
    cur_s,cur_e = lines[i][0],lines[i][1]
    if cur_s < pre_e: #현재_s <이전_e -> 둘이 겹치는 부분 존재
        if cur_e < pre_e:#두번째케이스 -> 아예 현재값이 이전값 안에 있는 경우
            continue
        else: #한쪽만 겹치는 경우
            length +=  cur_e - pre_e #현재_e - 이전_e 길이 더해줌
    else: #겹치는 부분이 존재하지 않는다면
        length += cur_e - cur_s #현재선분길이만 더해줌
    pre_s,pre_e = cur_s,cur_e #현재값을 전값으로 업데이트 해줌
print(length)
```
