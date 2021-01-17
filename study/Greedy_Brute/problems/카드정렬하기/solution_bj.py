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

