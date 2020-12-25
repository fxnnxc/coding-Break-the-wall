import sys
T = sys.stdin.readline()
for i in range(int(T)):
    N = int(sys.stdin.readline())
    m = [list(map(int, sys.stdin.readline().split())) for i in range(2)]
    for i in range(N-1):
        m[0][i+1] = max(m[0][i], m[1][i]+m[0][i+1])  
        m[1][i+1] = max(m[1][i], m[0][i]+m[1][i+1])
    print(max(m[0][-1], m[1][-1]))