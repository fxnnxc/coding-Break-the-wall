import sys 
from heapq import heapify, heappush, heappop

N = int(sys.stdin.readline())
times = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
times.sort()

starts = [i[0] for i in times]
end = times[-1][0]
heap = []
heapify(heap)
max_number = 0
index = 0
for t in starts:
    # 뽑는 부분
    while index<len(times) and times[index][0]<=t: 
        heappush(heap, times[index][1])
        index +=1
    # 힙에서 제거하는 부분
    while heap and heap[0]<=t:
        heappop(heap)

    # 힙 크기를 저장
    max_number = max(max_number, len(heap))

print(max_number)