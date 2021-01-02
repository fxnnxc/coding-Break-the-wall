# 이진트리 탐색


## [문제](https://www.acmicpc.net/problem/5639)

트리 정보에 대한 전위 순회 결과가 주어질 때, 후위 순위 정보를 찾는 문제. 


```
50 30 24 5 28 45 98 52 60
50 30  24 | 5 | 28 45 98 52 60
50 | 30 | 24 ` 0 ` 28 45 98 52 60
왼쪽 오른쪽 가운데를 Recursive하게 나누고 [A B~~~  C~~~] 출력  

출력
5 28 24 45 30 60 52 98 50
```


## Solutions
|solution|time|info|
|:-:|:-:|:-:|
|[solution1.py](solution1.py)|880ms|python3는 시간초과가 난다. |
|[solution2.py](solution2.py)|X|tree의 리스트 버전, 시간 초과가 난다. |
