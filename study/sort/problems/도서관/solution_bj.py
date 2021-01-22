def count_step(lst, k):
    step = 0
    for i in range(len(lst)-1,-1, -k):
        step += 2*lst[i]
    return step 

N, M = map(int, input().split())
lst = list(map(int, input().split()))

step = 0
plus_lst = [i for i in lst if i>0]+[0]
minus_lst = [-i for i in lst if i<0]+[0]

plus_lst.sort(reverse=False)   # 9 8 7 6 
minus_lst.sort(reverse=False)  

if plus_lst[-1]>=minus_lst[-1]:
    step += plus_lst[-1]
    for i in range(M):
        if plus_lst:
            plus_lst.pop()
        else:
            break
else:
    step += minus_lst[-1]
    for i in range(M):
        if minus_lst:
            minus_lst.pop()
        else:
            break

# 플러스 정리
step += count_step(plus_lst, M)

# 마이너스 정리
step += count_step(minus_lst, M)

print(step)