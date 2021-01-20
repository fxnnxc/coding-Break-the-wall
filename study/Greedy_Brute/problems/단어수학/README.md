# 단어 수학

## 문제
* [link](https://www.acmicpc.net/problem/1339)

## 풀이
N = int(input())
lst = []
answer=[]
for i in range(N):
    lst.append(list(input()))
dic={}

# A가 3자리 수이면 100 2자리 수이면 10 이런 식으로 사전에 더하기
for i in range(N):
    for j in range(len(lst[i])):
        if lst[i][j] in dic.keys():
            dic[lst[i][j]] += 10**(len(lst[i])-j-1)     
        else:
            dic[lst[i][j]] = 10**(len(lst[i])-j-1)

# 사전의 값을 sort하기 위해서 리스트로 변환 
for key,value in dic.items():
    answer.append([key,value])

# 1 인덱스 기준으로 내림차순
answer.sort(key= lambda x:-x[1])

# 큰 수 부터 9 , 8 , ..1 로 라벨링
c=10
for i in range(len(answer)):
    c-=1
    answer[i][1]=c #[['A', 9], ['C', 8], ['G', 7], ['D', 6], ['E', 5], ['F', 4], ['B', 3]]

# lst의 값들을 answer의 라벨로 replace
for i in range(len(lst)):
    for j in range(len(lst[i])):
        for k in range(len(answer)):
            if lst[i][j] ==answer[k][0]:
                lst[i][j] = str(answer[k][1])
                break

# lst = [['7', '8', '4'], ['9', '8', '6', '5', '3']]
for i in range(len(lst)):
    lst[i] = "".join(lst[i])

ans = 0
for i in lst:
    ans = ans + int(i)

print(ans)
