def possible(lessons, M, blue):
    summ = 0
    count = 1
    for i in lessons:
        summ+=i
        if summ>blue:
            summ=i
            count +=1
        if count>M:
            return False
    return True

N, M = map(int, input().split())
lessons = list(map(int, input().split()))
left, right = max(lessons), sum(lessons)
# 최소를 구하는 문제
while left<right:
    mid = (left+right)//2
    if possible(lessons, M, mid):
        right = mid
    else:
        left = mid+1
print(left)
