def solution(N):
    dp = [1 for i in range(10)]
    for i in range(1, N):
        for i in range(0, 10):
            dp[i] += sum(dp[i+1:])
    return sum(dp)

N = int(input())
print(solution(N)%10007)