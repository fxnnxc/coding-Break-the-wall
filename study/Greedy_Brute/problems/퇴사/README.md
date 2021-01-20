# 퇴사

## [문제](https://www.acmicpc.net/problem/14501)

퇴사를 진행행하려 하는는데 N+1일 째 되는날 퇴사를 하기 위해서 N일 동안 많은 상담을 하려고 한다.

상담을 완료하는데 걸리는 시간 T와 상담을 했을 때 받을 수 있는 금액 P를 보고, 퇴사 전까지 최대 수익을 구하는 문제이다.

## 예제

|     | 1일 | 2일 | 3일 | 4일 | 5일 | 6일 | 7일 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ti  | 3   | 5   | 1   | 1   | 2   | 4   | 2   |
| Pi  | 10  | 20  | 10  | 20  | 15  | 40  | 200 |

```
입력
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

출력
45

```

## 문제 풀이 전략

| day | 0   | 1   | 2   | 3   | 4   | 5   | 6   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ti  | 3   | 5   | 1   | 1   | 2   | 3   | 2   |
| Pi  | 10  | 20  | 10  | 20  | 15  | 40  | 200 |

day는 0~n-1, 퇴사일 n
dp 방식으로 푼다

- dp[day] = max(dp[day+1],dp[day+T[day]]+P[day])

- day에서 시작해서 퇴사일까지의 수익의 최댓값을 dp[day]에 저장
  ex) dp[0]에는 0일부터 퇴사할 때까지의 최댓값을 저장

dp[day]에는 두 가지 중에서 **최댓값**을 저장

- 오늘의 스케줄을 안 하는 경우
  dp[day+1] : 오늘의 스케줄을 안하는 경우는 날짜를 하나 넘기면 됨
- 오늘의 스케줄을 하는 경우
  dp[day +T[day]]+P[day] : day[0]의 스케줄을 했다면 0 더하기 day[0]을 소화하는데 걸리는 기간인 T[day]를 더해주고, 스케줄을 소화했기 때문에, day[0]에서 줄 수 있는 금액인 P[day]를 더해준다.

dp[day] = max(dp[day+1],dp[day+T[day]]+P[day])

solve(0) = max(solve(1),solve(3)+10) = 45
solve(1) = max(solve(2),solve(6)+20) = 45
solve(2) = max(solve(3),solve(3)+10) = 45
solve(3) = max(solve(4),solve(4)+20) = 35
solve(4) = max(solve(5),solve(6)+15) = 15
solve(5) = max(solve(6),solve(8)+40) = 0
solve(6) = max(solve(7),solve(8)+200) = 0
solve(7) = 0
solve(8) = -무한대
solve(8)부터는 9일에 퇴사하는게 되어버림

## Results

|           Version            | Memory  | Time(ms) | info     |
| :--------------------------: | :-----: | :------: | :------- |
| solution1.py([solution1.py]) | 28776KB |   64ms   | Baseline |

## Solution 1

```python
def solve(t,p):
    max_pay = 0 #지금까지 최대페이
    for day in range(n):
        max_pay = max(max_pay,dp[day])
        if day+t[day] > n:
            continue
        dp[day+t[day]] = max(dp[day+t[day]],max_pay+p[day])
        #max(일을 안 하고 넘어갈 경우 페이,현재 day까지와서 벌은 돈의 최댓값 + 현재 일을 할 경우 페이)

    print(max(dp))

if __name__ == "__main__":
    n = int(input())
    t,p = [0]*n,[0]*n
    dp = [0]*(n+1)

    for i in range(n):
        t[i], p[i] = map(int, input().split())

    solve(t,p)


```
