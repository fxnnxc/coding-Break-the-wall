# The Great Revegetation

## 문제 



```
input
3 2
S 1 2
D 3 2

output
10

```

## 풀이
```
N = 농작지의 길이
M = 소의 마리 수 
ㅁㅁㅁ 세 칸이 있을 때, 
첫 번째 소는 1 2 칸에 똑같은 타입의 작물을 심어야 한다. 
두 번째 소는 3,2 칸에 다른 작물을 심어야 한다. 

A A B
B B A
2 -> 이진수 -> 10 
```


## Solutions

|Solution|info|
|[solution1.py](solution1.py)|unsloved, timeout|
|[solution2.py](solution2.py)|unsloved, timeout|
|[solution3.py](solution3.py)|unsloved, type이 같은 애들끼리 묶음. timeout|
|[solution4.py](solution4.py)|unsloved, type이 같은 애들끼리 비교를 빠르게 함.  timeout|