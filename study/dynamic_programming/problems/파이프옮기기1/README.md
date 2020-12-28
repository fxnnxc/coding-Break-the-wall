# 파이프 옮기기

## [문제](https://www.acmicpc.net/problem/17070)



## results
|source|mem|time|
|---|---|---|
|[solution1.py](solution1.py)|29M|64ms|


## Solution

```python
def solution(N, b):
    dpV = [[0 for i in range(N)] for j in range(N)]
    dpH = [[0 for i in range(N)] for j in range(N)]
    dpD = [[0 for i in range(N)] for j in range(N)]
    dpH[1][0] = 1
    for i in range(N):
        for j in range(N):
            # The case when end point lies in i,j index
            #Horizontal
            if 0<=j-2 and b[j-1][i]+b[j][i]+b[j-2][i]==0: 
                    dpH[j][i] += dpH[j-1][i]
                    if i-1>=0 and b[j-2][i-1]+b[j-1][i-1]==0:
                        dpH[j][i]+=dpD[j-1][i]
            
            #Vertical
            if 0<=i-2 and b[j][i-1]+b[j][i]+b[j][i-2]==0: 
                    dpV[j][i] += dpV[j][i-1]
                    if j-1>=0 and b[j-1][i-2]+b[j-1][i-1]==0:
                        dpV[j][i]+=dpD[j][i-1]
            # Diagonal 
            if 0<=j-1 and 0<=i-1 and b[j-1][i-1]+b[j][i-1]+b[j-1][i]+b[j][i]==0:
                if j-2>=0 and b[j-2][i-1]==0:
                    dpD[j][i] +=dpH[j-1][i-1]
                if 0<=i-2 and b[j-1][i-2]==0:
                    dpD[j][i] +=dpV[j-1][i-1]
                if 0<=j-2 and 0<=i-2 and  b[j-2][i-1]+b[j-1][i-2]+b[j-2][i-2]==0:
                    dpD[j][i] +=dpD[j-1][i-1]
            
            
    return dpD[-1][-1]+dpH[-1][-1]+dpV[-1][-1]           
            

N = int(input())
board = [ list(map(int, input().split())) for i in range(N)] 
board_reverse = [[0 for i in range(N)] for j in range(N)]    # Because I made a mistake for selecting column and row in 'def solution()' 
for i in range(N):
    for j in range(N):
        board_reverse[i][j] = board[j][i]

print(solution(N, board_reverse))
```
