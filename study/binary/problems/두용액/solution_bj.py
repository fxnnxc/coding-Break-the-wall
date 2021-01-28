def find_closest(v, lst):          
    left_idx, right_idx = 0, len(lst)-1
    while 1 < right_idx - left_idx :
        mid_idx = (left_idx+right_idx)//2 
        mid = lst[mid_idx]
        if v <= mid: 
            right_idx = mid_idx
        else:
            left_idx= mid_idx

    if lst[right_idx] -v < v-lst[left_idx]:
        return lst[right_idx]
    else:
        return lst[left_idx] 

def solution(lst):
    alc = [i for i in lst if i<0]
    acd = [i for i in lst if i>0]
    alc.sort()
    acd.sort()
    if len(alc)==0 or len(acd)==0:
        ret = alc[-2:] if alc else acd[:2]
    else:
        if len(alc)>1:
            mini = abs(alc[-1]+alc[-2]) 
            r1,r2 = alc[-1], alc[-2]
        if (len(acd)>1 and len(alc)>1 and  abs(acd[0]+acd[1]) < mini):
                mini = abs(acd[0]+acd[1])
                r1,r2 = acd[0], acd[1]
        elif len(acd)>1:
            mini = abs(acd[0]+acd[1])
            r1,r2 = acd[0], acd[1]
        for c in alc:
            v = find_closest(-c, acd)
            if abs(c+v) < mini:
                mini = abs(c+v)
                r1,r2 = c, v
        ret = sorted([r1, r2])
    for r in ret:
        print(r, end=" ")

N = int(input())
lst = list(map(int, input().split()))
solution(lst)

