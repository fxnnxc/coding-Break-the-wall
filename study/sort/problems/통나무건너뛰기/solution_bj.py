from collections import deque 

abs = lambda x:x if x>0 else -x

def solution(lst):
    lst.sort(reverse=True)
    temp = deque()
    for i,j  in enumerate(lst):
        if i%2==0:
            temp.append(j)
        else:
            temp.appendleft(j)
            
    MAX = abs(temp[0]-temp[-1])
    for i in range(len(temp)-1):
        MAX = max(MAX, abs(temp[i+1]- temp[i]))
    print(MAX)

T = int(input())
for i in range(T):
    n= int(input())
    lst = list(map(int, input().split()))
    solution(lst)