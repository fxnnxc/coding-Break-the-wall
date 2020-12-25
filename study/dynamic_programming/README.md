### [ACMIC Problem Link 👨‍💻👩‍💻](https://www.acmicpc.net/group/practice/9719/1)

---

# Dynamic Programming

## What is Dynamic Programming?

* 주어진 문제를 풀기 위해서, 문제를 여러 개의 하위 문제(subproblem)로 나누어 푼 다음, 그것을 결합하여 최종적인 목적에 도달하는 방법


#### 특징
## 재귀적 해법의 장단점
예: Fibonacci 수 구하기
𝑓_𝑛=𝑓_(𝑛−1)+𝑓_(𝑛−2)
아주 간단한 문제지만 Dynamic programming의 동기와 구현이 다 포함되어 있다

## Recursive Algorithm
<pre>
<code>
fib(n) 
{ 
        if (n == 1 or n == 2) then
            return 1; 
        else
            return (fib(n-1) +fib(n-2)); 
} 
</code>
</pre>
-> 엄청난 중복 호출이 존재한다

## 🍔 피보나치수를 구하는 DP Algorithm
<pre>
<code>
fibonacci(n) 
{ 
        f[1] ← f[2] ← 1; 
        for i ← 3 to n 
                f[i] ← f[i-1] +f[i-2]; 
        return f[n]; 
} 
</code>
</pre>
-> O(n)

동적계획법에서 아주 중요한 개념
함수의 값을 계산한 뒤 계산된 값을 배열에 저장하는 방식
필요한 때마다 함수를 다시 호출하지 않고 값을 빠르게 가져올 수 있음

## DP의 적용 요건 및 방법
### Optimal substructure
큰 문제의 최적 솔루션에 작은 문제의 최적 솔루션이 포함됨
### Overlapping recursive calls
재귀적 해법으로 풀면 같은 문제에 대한 재귀 호출이 심하게 중복됨
### 작은 크기 입력에 대한 최적 Solution -> 큰 입력에 대한 최적 Solution


---
# Problems

## Assigned 📌

|name|solution|key words|
|:-:|:-:|:-:|
|듣보잡|[UnSolved](problems/듣보잡)|
|그대로 출력하기2|[UnSolved](problems/그대로출력하기2)|
|가장 긴 바이토닉 부분 수열|[Solved](problems/가장긴바이토닉부분수열)|
|잃어버린 괄호|[Solved](problems/잃어버린괄호) |괄호, 아이디어, 괄호순서 정하기, 아이디어로 쉽게 해결

## Free 🤗

자유롭게 풀고 풀이를 올린 문제

|name|solution|key words|info|
|:-:|:-:|:-:|:--|
|다리놓기|[Solved](problems/다리놓기)|경우의 수 조합, 쉬움|---|
|스티커|[Solved](problems/스티커)|DP memory사용|<img src="https://latex.codecogs.com/gif.latex?\underset{2\times&space;N}{Matrix},&space;\underset{2\times&space;2}{dp}" width=100> |
