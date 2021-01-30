


# 압축

* link 

https://www.acmicpc.net/problem/1662


## 문제

압축된 문자열이 주어졌을 때, 압축을 푼 문자열의 길이를 구하는 문제

## 규칙
* 괄호가 있을 경우, 괄호 안을 괄호 앞의 숫자로 반복한다. 
* ```K(Q)``` 는 Q라는 문자열이 K번 반복됨을 나타낸다.  

```
ex1 
33(562(71(9)))

result
9
```


## 풀이

* [N, L]로 생각한다. L은 마지막 숫자를 나타내고, L은 길이를 나타낸다. 
* K(Q) --> [KQ, Q[-1]]
* K([N, L]) --> [KN, L]
* Q[N,L] --> [N+Q, L] 로 바꾼다. 
```
33(562(71(9)))
```

```python

K()

(12345) -> [5, 5]
(235235[5,5]1236) -> [11,5]1236 -> [15, 6]
(123[5,5]5235[1,2]) -> [8,5] 
count = 0
start =False
L = None
for i in Q:
    if i=="[":
        start = True
        stack = []
    if i=="]":
        start = False
        N, L = "".join(stack).split(",")
        count +=N
    if not start:
        count +=1
        L= i
    else:
        stack.append(i)
```