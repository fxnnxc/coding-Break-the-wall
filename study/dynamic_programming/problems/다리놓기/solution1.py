import sys 

def combination(K,N):
    # return the number of combinations
    # nCk = n!/(k!) = n~(n-k+1)
    ret = N 
    for i in range(N-1, N-K, -1):
        ret *= i
    for i in range(1, K+1):
        ret //= i
    return int(ret)





T = int(sys.stdin.readline())

for i in range(T):
    N, K = map(int, sys.stdin.readline().strip().split())
    print(combination(N,K))
