T = int(input())
for i in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for i in range(2)]
    dp = [[0 for i in range(N)] for j in range(2)] # 각 위치에서 최대값을 보관한다. 
    dp[0][0] = mat[0][0]
    dp[1][0] = mat[1][0]

    for i in range(N-1):
        dp[0][i+1] = max(dp[0][i], dp[1][i]+mat[0][i+1])  
        dp[1][i+1] = max(dp[1][i], dp[0][i]+mat[1][i+1])

    print(max(dp[0][-1], dp[1][-1]))