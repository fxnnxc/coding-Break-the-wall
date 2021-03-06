import sys 
sys.setrecursionlimit(3000)

dx = [1,1,1,-1,-1,-1,0,0,0]
dy = [0,1,-1, 0,1,-1, 0,1,-1]

def bfs(board, x, y):
    if board[y][x] ==1:
        board[y][x] = 0
        for i in range(9):
            board[y][x]=2
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<len(board[0]) and 0<=ny<len(board):
                bfs(board, nx, ny)


def solution(a,b, board): # board is b x a matrix
    current = 0
    for y in range(b):
        for x in range(a):
            if board[y][x]==1:
                bfs(board,x,y)
                current +=1
    return current


while True:
    a,b = map(int, sys.stdin.readline().strip().split())
    if a==0 and b==0:
        break
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(b)]
    print(solution(a,b,board))
