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


*를 임의의 연산이라고 가정하자. 

[A * B] * C 의 값이 있을 때, 연산 순서를 바꾸는 것과 바꾸지 않는 것의 크기 차이를 비교해서 최소가 되는 것을 선택한다. 

A * B는 이미 최소가 되는 연산으로 선택되었다. 그러나 B * C가 전체 크기를 더 줄일 수도 있다. 
따라서 두 개의 경우를 비교해서 최소로 하는 것은 전체 값을 최소로 하는 것이다. 

## Results
|Version|Memory|Time(ms)|info|
|:-:|:-:|:-:|:--|
|[solution1.py](solution1.py)|33M|140|Baseline|


## Best solution

```python

```

## DP strategy
```python

```
