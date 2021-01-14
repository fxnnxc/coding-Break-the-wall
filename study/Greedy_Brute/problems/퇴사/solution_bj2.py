N = int(input())
lst = [list(map(int, input().strip().split())) for i in range(N)]

dp = [0 for i in range(N+1)]
for t in range(N-1,-1,-1):
    du, re = lst[t]
    if du+t <=N:
        dp[t] = max(dp[t+du]+re, dp[t+1])
    else:
        dp[t] = dp[t+1]
            

print(dp[0])