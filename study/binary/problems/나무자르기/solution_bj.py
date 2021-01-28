import sys 

def possible(v, M, lst):
    summ = 0
    for i in lst:
        if i-v>0:
            summ+=i-v
        if summ>=M:
            return True 
    return False

# 나무를 최소한으로 가져가기
N, M = map(int, input().split())
lst = list(map(int,input().split()))
left, right = 0, max(lst)
while left<right:
    mid = (left+right)//2+1    
    if possible(mid, M, lst): # 중간 나무를 잘라도 가능하면, 왼쪽을 옮긴다. 
        left = mid
    else:  # 불가능하다면, 오른쪽을 줄인다. 
        right = mid-1

print(left)