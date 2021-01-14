def solution(a,b,count):
    if a==b:
        lst[0] = min(lst[0], count)
        return True
    elif a<b:
        if solution(int(str(a)+"1"),b, count+1):
            return True
        if solution(a*2,b, count+1):
            return True 



a, b = map(int, input().strip().split())
lst=[b]
solution(a,b,0)
if lst[0]==b:
    print(-1)
else:
    print(lst[0]+1)