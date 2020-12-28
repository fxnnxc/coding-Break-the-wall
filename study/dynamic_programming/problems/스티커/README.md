# 스티커 


## [문제](https://www.acmicpc.net/problem/9465) 

* 2xN 스티커에서 하나를 찢으면 양쪽과 위쪽을 사용할 수 없게 된다. 
* 스티커에 써진 합이 최대가 되도록 스티커를 찢는 방법. 
  


```
입력   
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80

출력   
260
290

cat examples/ex1 | python solution1.py
```

## 풀이전략
* 위쪽과 아래쪽을 선택하는 문제로 생각한다. 
* 위쪽을 선택했을 때의 최대값과 아래쪽을 선택했을 때의 최대값을 저장
* 최대값을 저장하기 위한 메모리 dp를 사용. 

## SUDO
```python

S = [2xN] matrix
dp = [2xN] matrix 



```



## 고민

## Solution 

|version|memory|time|info|
|---|---|---|---|
|[solution1.py](solution1.py)|47M|1108ms|2xN matrix사용. dp값을 계속 저장<br/> dp+= 실수  |
|[solution2.py](solution2.py)|**40M**|**1000ms**|2x2 matrix사용. |
|[solution3.py](solution3.py)|46M|1000ms|dp=MAX 로 solution1의 실수 고침. |
|[solution4.py](solution4.py)|44M|1000ms|dp 매트릭스를 할당하지 않고 mat에서 처리<br/>+코드 최소화 |

---


## Best Solution
```python
T = int(input())
for i in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for i in range(2)]
    dp = [[0 for i in range(2)] for j in range(2)] # 메모리를 최적화하기

    dp[0][0] = mat[0][0]
    dp[1][0] = mat[1][0]
    
    for i in range(N-1):
        right, left = (i+1)%2, i%2
        dp[0][right] = max(dp[0][left], dp[1][left]+mat[0][i+1])  
        dp[1][right] = max(dp[1][left], dp[0][left]+mat[1][i+1])

    print(max(dp[0][right], dp[1][right]))
```
