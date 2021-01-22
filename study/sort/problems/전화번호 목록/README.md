# 전화번호 목록

* [link](https://www.acmicpc.net/problem/5052)

## 풀이

String 크기 비교를 활용한다. 

```
911
9762599
91125426

<<<<<
sort 
>>>>>

911 91125426 9762599
```

```911```은 ```91125426```보다 크며, ```911``` 뒤에 붙는 숫자 ```911XXX``` 는 ```911``` 바로 뒤에 위치하게 된다. 

이는 문제에서 요구하는 바와 일치한다. 

## Solution

```python
import sys 
def solution(lst):
    lst.sort()  # string 크기 비교로 정렬한다. 
    for i in range(len(lst)-1):
        # 앞의 원소가 뒤의 원소와 일치하면 번호가 눌린다. 
        if lst[i]==lst[i+1][:len(lst[i])]:   
            print("NO")
            return 
    print("YES")
    return 

T = int(input())
for i in range(T):
    N = int(sys.stdin.readline().strip())
    lst = [sys.stdin.readline().strip() for i in range(N)]
    solution(lst)
```