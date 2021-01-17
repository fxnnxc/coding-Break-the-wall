# 카드 정렬하기

* [link](https://www.acmicpc.net/problem/1715)

## 문제

N개의 카드 뭉치가 있을 때, 카드를 합치는데는 A+B의 연산이 필요하다. 

총 연산 수를 최소화하면 합치는 방법에 대한 문제. 

HEAP을 사용하면 좋다. 


## Solution
```python
import sys
from heapq import heapify, heappop, heappush 

N = int(input())
heap = [int(sys.stdin.readline()) for a in range(N)]
heapify(heap)
count = 0
while len(heap)!=1:
    sm, lg = heappop(heap), heappop(heap)
    count +=sm+lg
    heappush(heap, sm+lg)
    
print(count)

```