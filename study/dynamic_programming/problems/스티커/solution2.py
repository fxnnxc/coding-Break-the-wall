T = int(input())
for i in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for i in range(2)]
    dp = [[0 for i in range(2)] for j in range(2)] # 메모리를 최적화하기

    dp[0][0] = mat[0][0]
    dp[1][0] = mat[1][0]
    
    for i in range(N-1):
        right, left = (i+1)%2, i%2
        dp[0][right] = max(dp[0][left], dp[1][left]+mat[0][i+1])  
        dp[1][right] = max(dp[1][left], dp[0][left]+mat[1][i+1])

    print(max(dp[0][right], dp[1][right]))