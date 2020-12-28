# 가장 긴 바이토닉 부분 수열

## 문제

수열이 주어질 때, 부분 수열 중에서 가장 긴 바이토닉 부분 수열의 길이를 찾는 문제이다. 

## 문제 전략

기존 부분 수열 A가 있을 때, 새로운 원소 a가 들어온다면 어떻게 가장 긴 바이토닉 부분 수열을 만들지 생각. 

조건에 따라서 a를 추가한 경우가 가장 긴 바이토닉 부분수열을 만든다면 a를 추가한 수열이 새로운 A가 된다. 

1 4 6 3 1 2 -> 최소인 1이랑 바뀐다. 
mid = 6 

만일 a를 추가하는 것이 좋지 못하다면 건너 뛴다. 


1 5 2 1 4 3 4 5 2 1

1 2 3 4 5 2 1 

## Results

|Code|memory|time|
|:-:|:-:|:-:|
|[solution1.py](solution1.py)|29M|180ms|increasing and decreasing|
|[solution2.py](solution2.py)|29M|200ms|do not assign value|
