# 다리놓기 


## [문제](https://www.acmicpc.net/problem/1010) 

* 왼쪽에서 오른쪽으로 겹치지 않고 다리를 놓을 수 있는 개수를 찾는 문제
* 왼쪽 수(k)는 오른쪽(n)보다 작기 때문에, nCk 조합 수를 계산하는 문제이다. 



```
입력   
3
2 2
1 5
13 29

출력   
1
5
67863915

cat examples/ex1 | python solution1.py
```

## 고민

나눠주는 부분에서 실수 나눗셈을 하니까 틀렸음. 

반드시 정수 나눗셈을 해야한다. (Precision에서 문제가 생기는 듯하다. )

## Solution 

|version|memory|time|info|
|---|---|---|---|
|[solution1.py](solution1.py)|29M|68ms|nCk를 for문으로 구성|

---

