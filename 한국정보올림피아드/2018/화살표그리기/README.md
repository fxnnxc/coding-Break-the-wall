# 화살표 그리기

[문제 링크](https://www.acmicpc.net/problem/15970)


## 문제 이해   
0, 1, 2, ...와 같은 음수가 아닌 정수들이 일정한 간격으로 오른쪽 방향으로 놓여 있다.
이러한 위치들 중 N개의 위치에 하나씩 점들이 주어진다
점은 위치와 색깔 정보를 가진다.

예를 들어, 점들을 순서쌍 (위치, 색깔) 로 표시할 때, a = (0, 1), b = (1, 2), c = (3, 1), d = (4, 2), e = (5, 1)라고 하자.
a, c, e 끼리 같은 색을 가지는 데, a에서 거리가 가까운 수는 c, e에서 거리가 가까운 수는 c,
c에서 거리가 가까운 수는 자신의 양쪽의 수의 위치정보를 고려하기 때문에 e라고 할 수 있다.

이처럼 각 점마다 (나가는) 화살표를 하나씩 그릴 수 있고, 화살표를 그릴 때의 기준은 다음과 같다.
1. 색이 같아야 하며
2. 자신과 거리가 가장 가까운 한 점에만 그리기 가능

화살표를 다 그리고 그려진 모든 화살표의 길이의 총 합을 구하는 것이 문제의 핵심


## 풀이 전략
1. 색이 같은 모든 점들을 찾는다. 
2. 그 점들의 위치정보를 하나의 리스트 안에 넣어준다.
3. 그 리스트를 ' **화살표 길이의 합을 계산하는 함수'** 에 넣는다. (같은 색을 가져야만 화살표를 그릴 수 있음)
4. 색 별로 이 함수에 넣어서 나온 출력값을 모두 더해준다.


## 고민
입력은 어떻게 받아야 하는가..?

### 고민 해결
1. input()
2. sys.stdin.readline : 속도가 더 빠름

## Source Code
<pre>
<code>
#입력
5
0 1
1 2
3 1
4 2
5 1

#출력
20
</code>
</pre>

<pre>
<code>
#같은 색깔을 가진 원소들의 화살표 총길이를 계산하는 함수
def distance(a):
    leng = 0 
    for i in range(len(a)):
        if i == 0:#맨앞
            leng += abs(a[i] - a[i + 1])
        elif i == len(a) - 1: #맨뒤
            leng += abs(a[i] - a[i - 1])
        else:
            # i + 1 과 i - 1 까지의 차이를 비교해서 작은 친구를 채택
            leng += min(abs(a[i] - a[i - 1]), abs(a[i] - a[i + 1]))
    return leng


#main
n = int(input()) #점의 갯수
answer = 0 #출력값 변수
arr_swp = [] #점의 정보를 닮을 리스트

for i in range(n):
    loc, clr = map(int, input().split())
    arr_swp.append([clr, loc]) #[[1, 0], [2, 1], [1, 3], [2, 4], [1, 5]]
arr_swp.sort() #[[1, 0], [1, 3], [1, 5], [2, 1], [2, 4]]


#색의 갯수
num_clr = arr_swp[-1][0] 
for i in range(1,num_clr+1):#색의 갯수는 1부터 존재
		same_clr = [] #같은 색인 점들의 위치정보를 모으는 리스트
    for j in range(n): #원소의 갯수 만큼 반복
        if arr_swp[j][0] == i:
            same_clr.append(arr_swp[j][1])
    answer += distance(same_clr)

print(answer)
</code>
</pre>

