import sys 

def isCatchable(x,y,px, L):
    if abs(x-px)+y <=L:
        return True 
    else:
        return False

def solution(pos, animals, L):
    count = 0
    for x,y in animals:
        # 동물의 x에서 거리가 제일 가까운 p를 찾는다. 
        # p를 기준으로 동물을 찾으면 시간 초과가 날듯
        left, right = 0, len(pos)-1
        while 0 < right-left :
            mid = (left+right)//2
            if pos[mid] >= x: 
                right = mid
            else:
                left = mid+1
        if isCatchable(x,y, pos[left], L) or isCatchable(x,y, pos[left-1], L):  # left =mid +1 이라서, 넘어갈 수도 있음
            count +=1
    return count


M, N, L = map(int, input().split())
pos = list(map(int, input().split()))
animals = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
pos.sort()  # Binary Search를 위한 정렬
print(solution(pos, animals, L))