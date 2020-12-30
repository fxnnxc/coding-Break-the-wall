# 그대로 출력하기 2

## [문제](https://www.acmicpc.net/problem/11719) 
입력 받은 대로 출력하는 프로그램을 작성하시오.

## 예제

[입력]<br>
    Hello

Baekjoon     
   Online Judge 
   
[출력]<br>
    Hello

Baekjoon     
   Online Judge 

## 문제 풀이 전략
[처음 소스]
~~~
while True:
    try :
        print(input())
    except EOFError:
        break
~~~
처음엔 input() 사용했지만
input()보다 입출력 속도가 빠른  sys.stdin.readline() 사용

[수정 후 소스]
~~~
import sys
text = sys.stdin.read().splitlines()

for t in text :
    print(t)
~~~

여기서 splitlines()는 라인단위로 문자열을 나눠준다.
