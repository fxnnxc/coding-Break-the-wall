
def increasing_sub_sequence(lst):
    # return the length of maximum increasing sub sequence
    dp = [1 for i in range(len(lst))]
    for i in range(1, len(lst)):
        for j in range(i):         #including itself.
            if dp[j]>=dp[i] and lst[j]<lst[i]:
                dp[i]=dp[j]+1
    return dp

def decreasing_sub_sequence(lst):
    # return the length of maximum decreasing sub sequence
    dp = [0 for i in range(len(lst))]
    for i in range(len(lst)-1, -1, -1):
        for j in range(i, len(lst)):
            if lst[j]<lst[i] and dp[j]>=dp[i]:
                dp[i] = dp[j]+1
        
    return dp


def solution(lst):
    lst1 = increasing_sub_sequence(lst)
    lst2 = decreasing_sub_sequence(lst)
    MAX = 0
    for i,j in zip(lst1, lst2):
        if i+j > MAX:
            MAX = i+j
    # print(lst)
    # print(lst1)
    # print(lst2)
    return MAX


n = int(input())
lst = list(map(int, input().split()))
print(solution(lst))
