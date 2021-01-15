def isPossible(n, info):
    for num, stk, bal in info:
        str_cnt, bal_cnt = 0,0 
        for i in range(len(num)):
            if n[i]==num[i]:
                str_cnt +=1
            elif n[i] in num:
                bal_cnt +=1
        if str_cnt != int(stk) or bal_cnt != int(bal):
            return False 
    return True

"""
info : (Number, Strike, Ball) x N
"""
N = int(input())
info = [list(input().split()) for i in range(N)]
count = 0
for i in [k for k in range(1, 10)]:
    for j in [k for k in range(1, 10) if k!=i]:
        for t in [k for k in range(1, 10) if k!=i and k!=j]:
            if isPossible(f"{i}{j}{t}", info):
                count +=1
print(count)
