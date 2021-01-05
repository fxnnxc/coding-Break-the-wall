n = int(input()) # 부등호 개수
sign = input().split() #부등호
check = [False]*10 # 0~9
mx, mn = "", ""

# 부등호가 성립하는 지 확인하는 함수
def possible(i,j,k):
    if k == '<':
        return i<j
    if k == '>':
        return i>j
    return True

def solve(cnt, z):
    global mx, mn
    if cnt == n+1:
        if not len(mn): # mn이 비워져 있으면 최솟값에 z 넣기
            mn = z
        else: # mn에 값이 있으면 최댓값에 넣기
            mx = z
        return
    for i in range(10):# 0부터 9까지
        if not check[i]: # check[i]이 false이면(중복 방지)
            if cnt==0 or possible(z[-1], str(i), sign[cnt-1]):
                check[i]=True
                solve(cnt+1, z+str(i)) #재귀함수
                # 만약 0 > ? 일 경우 ?에 올 숫자가 없으므로 solve함수가 끝나고 check[0]이 false가 되고 check[1]부터 다시 시작한다.
                check[i]=False


solve(0, "") #solve 함수 돌리기
print(mx)
print(mn)
