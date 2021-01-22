import sys 
def solution(lst):
    lst.sort()
    for i in range(len(lst)-1):
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