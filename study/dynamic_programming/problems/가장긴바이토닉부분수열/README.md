# 잃어버린 괄호

## [문제](https://www.acmicpc.net/problem/11054) 
![image](https://user-images.githubusercontent.com/52944973/103066029-5a5bb700-45fb-11eb-8d3c-b6ed9c3ee0c8.png)

가장 긴 바이토닉 수열의 길이 찾기

## 예제

[1,50,2,3,4,2,5,4,3,10,2,1]

=>[1,2,3,4,5,4,3,2,1]이 가장 긴 수열이다.

cat examples/ex3 | python solution5.py
```

## 예시



## 문제 풀이 전략

가장 긴 증가하는 수열을 찾는 방법을 이용한다. 우선 가장 긴 증가하는 수열을 구한 뒤 (DP1),  주어진 리스트를 뒤집은 다음 다시 가장 긴 증가하는 수열을 구한다(DP2).
그 다음 DP2를 뒤집어서 DP!과 각 인덱스를 더한 뒤 max를 출력한다.


## Results



