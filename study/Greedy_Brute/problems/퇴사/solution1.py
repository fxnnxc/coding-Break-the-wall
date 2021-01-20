def solve(t,p):
    max_pay = 0 #지금까지 최대페이
    for day in range(n):
        max_pay = max(max_pay,dp[day])
        if day+t[day] > n:
            continue
        dp[day+t[day]] = max(dp[day+t[day]],max_pay+p[day])
        #max(일을 안 하고 넘어갈 경우,i번째까지 와서 벌은 돈의 최댓값 + 현재 i번째 일을 할 경우)

    print(max(dp))

if __name__ == "__main__":
    n = int(input())
    t,p = [0]*n,[0]*n
    dp = [0]*(n+1)

    for i in range(n):
        t[i], p[i] = map(int, input().split())

    solve(t,p)
