import sys 

def solution(lst, K):
    dp = [0 for i in range(K+1)]
    for i in range(K, -1, -1):
        for v in lst:
            if v<i:
                dp[i]+=dp[i-v]
            elif v==i:
                dp[i] +=1
    print(dp)
    return dp[-1]

N, K = map(int, sys.stdin.readline().strip().split())
values = [int(sys.stdin.readline().strip()) for i in range(N)]
print(solution(values, K))

