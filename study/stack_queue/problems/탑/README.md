# 탑

## 문제

## 풀이

```python
from heapq import heapify, heappop, heappush

N = int(input())
lst = list(map(int, input().split()))
heap = [[lst[-1], N-1]]
heapify(heap)
store = [0 for i in range(N)]
for i in range(N-1, -1,-1):
    while len(heap)>0 and lst[i]> heap[0][0]:
        index = heappop(heap)[1]
        store[index] = i+1
    heappush(heap, [lst[i], i])
for i in store:
    print(i, end=" ")
``` 
