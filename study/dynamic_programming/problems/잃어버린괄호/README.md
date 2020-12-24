# 잃어버린 괄호

## 문제 

괄호가 없는 식에 대해서 값을 최소로 만들기

## 예제

```
입력   55-50+40
출력   -35
```

## 예시

10-20+30-40-50 
   
이 식의 경우, 10 -(50) -90 = -130 으로 하는 경우가 최소가 나온다. 

만일, 순서 대로 계산하면 -10+30-90 = -70이 나온다. 


## 문제 풀이 전략


*를 임의의 연산이라고 가정하자. 

[A * B] * C 의 값이 있을 때, 연산 순서를 바꾸는 것과 바꾸지 않는 것의 크기 차이를 비교해서 최소가 되는 것을 선택한다. 

A * B는 이미 최소가 되는 연산으로 선택되었다. 그러나 B * C가 전체 크기를 더 줄일 수도 있다. 
따라서 두 개의 경우를 비교해서 최소로 하는 것은 전체 값을 최소로 하는 것이다. 

## Results
|Version|Memory|Time(ms)|info|
|:-:|:-:|:-:|:--|
|[solution1.py](solution1.py)|33M|140|Baseline|
|[solution2.py](solution2.py)|33M|128|using sys.stdin.readline|
|[solution3.py](solution3.py)|33M|128|remove assiging and reduce lines|
|[solution4.py](solution4.py)|29M|**64**|**add by plus first**</br> -10-(30+40+60)-(50+30+40)|
|[solution5.py](solution5.py)|29M|64|Do not use list(map(int, ...)) |



