import sys 
sys.setrecursionlimit(100000)

count = 0
N, M = map(int, input().split())
info = list(map(lambda x:(x[0], int(x[1])-1, int(x[2])-1), [sys.stdin.readline().strip().split() for i in range(M)]))

def evaluate(lst):
    for cow in info:
        cow_type, first, second = cow
        if first <len(lst) and second<len(lst):
            if cow_type =="S" and lst[first]!=lst[second]:
                return False 
            if cow_type =="D" and lst[first]==lst[second]:
                return False
    return True

def generate(lst, K):
    global count
    if not evaluate(lst):
        return
    if len(lst)==K:
            count +=1
    else:
        for i in ['A', 'B']:
            lst.append(i)
            generate(lst, K)
            lst.pop()

generate([], N)
print(f"{count:b}", end="")