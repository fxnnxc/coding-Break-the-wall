# 후위 표기식2

## [문제](https://www.acmicpc.net/problem/1935)

후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램

## 예제

```
입력
5
ABC*+DE/-
1
2
3
4
5

출력
1
AA+A+
1

```

## 문제 풀이 전략

피연산자가 나오면 숫자로 바꿔서 스택에 push,
연산자가 나오면 pop을 두 번해서, 두 번째 pop한 수에서 첫 번째 pop 한 수를 연산한다.

## Results

|           Version            | Memory  | Time(ms) | info                                |
| :--------------------------: | :-----: | :------: | :---------------------------------- |
| solution1.py([solution1.py]) | 28776KB |   64ms   | Baseline                            |
| solution2.py([solution2.py]) |    -    |    -     | 런타임에러/ex1에서 인덱스 에러가 뜸 |

## Solution 1

```python
n = int(input()) #피연산자 갯수
postfix = input()
nums = [0]*n
for i in range(n):
    nums[i] = int(input())
stack = []

for p in postfix:
    if 'A'<= p <= 'Z':
        stack.append(nums[ord(p)-ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        if p == '+':
            stack.append(a+b)
        elif p == '-':
            stack.append(a-b)
        elif p == '/':
            stack.append(a/b)
        elif p == '*':
            stack.append(a*b)

print('%0.2f' %stack[0])

```

## Solution 2

```python
n = int(input()) #피연산자 갯수
postfix = input()
nums = [0]*n
for i in range(n):
    nums[n-i-1] = int(input())
stack = []

for p in postfix:
    if 'A'<= p <= 'Z':
        stack.append(nums.pop())
    else:
        b = stack.pop()
        a = stack.pop()
        if p == '+':
            stack.append(a+b)
        elif p == '-':
            stack.append(a-b)
        elif p == '/':
            stack.append(a/b)
        elif p == '*':
            stack.append(a*b)

print('%0.2f' %stack[0])

# error
# Traceback (most recent call last):
#   File "solution2.py", line 10, in <module>
#     stack.append(nums.pop())
# IndexError: pop from empty list
```
