# 오르막수

## 문제
* [링크](https://www.acmicpc.net/problem/11057)
* 길이가 N인 오르막 수의 개수를 구하는 문제 
* 수는 0으로 시작할 수 있다. 

## 풀이 전략
* N에 대해서 오르막 수를 구했때, 마지막에 끝나는 수에 오르막 수를 더해준 게 N+1에 대한 오르막 수 이다. 


## Best solution

```python
def solution(N):
    dp = [1 for i in range(10)]
    for i in range(1, N):
        for i in range(0, 10):
            dp[i] += sum(dp[i+1:])
    return sum(dp)

N = int(input())
print(solution(N)%10007)
```

## Submission
|code|mem|time|
|---|---|---|
|[solution1.py](solution1.py)|29M|72ms|

