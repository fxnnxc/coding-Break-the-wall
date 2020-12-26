
def increasing_sub_sequence(lst):
    # return the length of maximum increasing sub sequence
    
    # 1 2 3 5 4
    dp = [1 for i in range(len(lst))]
    for i in range(1, len(lst)):
        cur = 1
        for j in range(i):
            if dp[j]>=cur and lst[j]<lst[i]:
                cur=dp[j]+1
        if cur>1:
            dp[i] = cur
    return dp

def decreasing_sub_sequence(lst):
    # return the length of maximum increasing sub sequence
    # 1 2 3 5 4
    dp = [1 for i in range(len(lst))]
    for i in range(len(lst), 0,-1 ):
        cur = 1
        for j in range(len(lst)-i):
            if dp[j]>=cur and lst[j]<lst[i]:
                cur=dp[j]+1
        if cur>1:
            dp[i] = cur
    return dp


def solution(lst):
    # 왼쪽부터 증가하는 부분 수열
    
    # 오른쪽부터 증가하는 수열
    # print(increasing_sub_sequence(lst))
    # print(decreasing_sub_sequence(lst))
    lst1 = increasing_sub_sequence(lst)
    lst2 = decreasing_sub_sequence(lst)
    MAX = 0
    for i,j in zip(lst1, lst2):
        if i+j > MAX:
            MAX = i+j
    return MAX



n = int(input())
lst = list(map(int, input().split()))
print(lst)
print(solution(lst))
















