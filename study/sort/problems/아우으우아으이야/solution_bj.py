import sys 
N = int(input())
lst = []
for i in range(N):
    x,y = map(int, sys.stdin.readline().strip().split())
    lst.append([x,y])
lst.sort()

length = 0
start = lst[0][0]
last = lst[0][1]

for i in range(1, len(lst)):
    x,y = lst[i]
    # overlap 
    if x<=last:
        last = max(y, last)
    # skip
    else:
        length += last - start 
        start, last = x, y

length += last - start 
print(length)

