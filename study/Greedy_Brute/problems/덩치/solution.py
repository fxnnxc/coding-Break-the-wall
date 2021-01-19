def solution(lst):
    for w,h in lst:
        rank = 1
        for j in range(len(lst)):
            if w < lst[j][0] and h < lst[j][1]:
                rank +=1
        print(rank, end=" ")

N = int(input())
lst = [list(map(int, input().strip().split())) for i in range(N)]
solution(lst)