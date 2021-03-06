### [ACMIC homework Link 👨‍💻](https://www.acmicpc.net/group/practice/9719/1)
### [All of Dynamic Programming Problems👩‍💻 ](https://www.acmicpc.net/problemset?sort=ac_desc&algo=25)
---

# Dynamic Programming

## Assigned 📌

|name|solution|key words|
|:-:|:-:|:-:|
|듣보잡|[Solved](problems/듣보잡)|
|그대로 출력하기2|[Solved](problems/그대로출력하기2)|
|가장 긴 바이토닉 부분 수열|[Solved](problems/가장긴바이토닉부분수열)|
|잃어버린 괄호|[Solved](problems/잃어버린괄호) |괄호, 아이디어, 괄호순서 정하기, 아이디어로 쉽게 해결

## Free 🤗

자유롭게 풀고 풀이를 올린 문제

|name|solution|key words|info|
|:-:|:-:|:-:|:--|
|다리놓기|[Solved](problems/다리놓기)|경우의 수 조합, 쉬움|---|
|스티커|[Solved](problems/스티커)|DP memory사용|<img src="https://latex.codecogs.com/gif.latex?\underset{2\times&space;N}{Matrix},&space;\underset{2\times&space;2}{dp}" width=100> |
|파이프옮기기1|[Solved](problems/파이프옮기기1)|DP 메모리 3개를 활용|
|오르막수|[Solved](problems/오르막수)|한 단계씩 DP 메모리를 이용해서 추가하는 문제 dp[i+1] +=dp[i] |


## What is Dynamic Programming?

* 주어진 문제를 풀기 위해서, 문제를 여러 개의 하위 문제(subproblem)로 나누어 푼 다음, 그것을 결합하여 최종적인 목적에 도달하는 방법


### 재귀적 해법의 장단점
* 예: Fibonacci 수 구하기 <img src="https://latex.codecogs.com/gif.latex?f_{n}=f_{n-1}+f_{n-2}" width=150px>

아주 간단한 문제지만 Dynamic programming의 동기와 구현이 다 포함되어 있다

### Recursive Algorithm
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

### 🍔 피보나치수를 구하는 DP Algorithm
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


### DP의 적용 요건 및 방법
* Optimal substructure
큰 문제의 최적 솔루션에 작은 문제의 최적 솔루션이 포함됨
* Overlapping recursive calls
재귀적 해법으로 풀면 같은 문제에 대한 재귀 호출이 심하게 중복됨
* 작은 크기 입력에 대한 최적 Solution -> 큰 입력에 대한 최적 Solution


---
