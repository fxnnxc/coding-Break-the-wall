# 듣보잡

## [문제](https://www.acmicpc.net/problem/1764) 

듣도 못한 사람과 보도 못한 사람의 수와 명단이 각각 주어질 때, 듣도 보도 못한 사람의 수와 명단을 출력하는 문제

## 예제

```
입력
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

출력
2
baesangwook
ohhenrie

```

## 예시

듣도 못한 사람은 3명 ohhenrie, charlie, baesangwook
보도 못한 사람은 4명 obama, baesangwook, ohhenrie, clinton

이러한 경우, 듣도 보도 못한 사람은 baesangwook, ohhenrie 으로 2명이 나온다. 

## 문제 풀이 전략

listen_list, see_list 에 input값을 넣고 name = set(listen_list) & set(see_list) 를 사용해서 겹치는 입력값을 구하고 sorted(list(name))를 통해 정렬하여 사전순서로 나오게 한다.


## Results
|Version|Memory|Time(ms)|info|
|:-:|:-:|:-:|:--|
|1764.py[1764.py]()|42496KB|3628ms|Baseline|


## Solution

```python
import sys
input = sys.stdin.readline

listen,see = map(int,input().split())
listen_list = []
see_list = []
for i in range(listen):
    listen_list.append(input().strip())
for i in range(see):
    see_list.append(input().strip())
name = set(listen_list) & set(see_list)
name = sorted(list(name))
print(len(name))
for i in name:
    print(i)
```

