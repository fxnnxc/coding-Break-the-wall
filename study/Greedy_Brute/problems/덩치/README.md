# 덩치

* [link](https://www.acmicpc.net/problem/7568)

## 문제 

리스트의 원소가 두 개일 때, 비교를 통해서 우위를 정하는 문제이다. 


```python 
def solution(lst):
    for w,h in lst:
        rank = 1
        for j in range(len(lst)):
            if w < lst[j][0] and h < lst[j][1]:
                rank +=1
        print(rank, end=" ")

N = int(input())
lst = [list(map(int, input().strip().split())) for i in range(N)]
solution(lst)
```