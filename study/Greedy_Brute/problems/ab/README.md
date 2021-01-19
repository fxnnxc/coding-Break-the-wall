# A->B

## 문제
* [link](https://www.acmicpc.net/problem/16953)

정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

```
[예제입력]
2 162
```

```
[예제출력]
5
```
2 → 4 → 8 → 81 → 162

## 풀이

2가지 방법으로 풀었다.
1. que에 넣어 dfs로 2를 곱하거나 1을 추가한 값이 B보다 작거나 같다면 que에 추가하여 반복해주는 것
2. B를 2로 나눠지면 2로 나누고, 끝자리가 1이면 1을 제거해준다. 만약 A보다 작아지거나 2로 나눌 수 없고 끝자리가 1이 아니라면 만들 수 없기 때문에 -1 출력해준다.

```
[1번 코드(272ms)]
a, b = map(int, input().split())
que = [(a, 1)]
result = -1
while que:
    x, cnt = que.pop(0)
    if x == b:
        result = cnt
        break

    if x*2 <= b:
        que.append((x*2, cnt+1))
    
    if int(str(x)+'1') <= b:
        que.append((int(str(x)+'1'), cnt+1))

print(result)
```
```
[2번코드(64ms)]
a, b = map(int, input().split())
que = [(b, 1)]
result = -1
while que:
    x, cnt = que.pop(0)
    if x == a:
        result = cnt
        break

    if x%2 == 0 and x/2>=a:
        que.append((x/2, cnt+1))
    elif x%10 == 1 and int(x/10) >= a:
        que.append((int(x/10), cnt+1))
    else:
        break

print(result)
```
