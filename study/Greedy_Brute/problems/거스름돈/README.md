# 거스름돈

천원에서 낸 돈에 대한 거스름돈을 동전의 개수를 최소한으로 하면서 내줄 때, 동전의 개수를 찾는 문제.

* [Link](https://www.acmicpc.net/problem/5585)
  
```python
n = int(input())
coin_types = [500, 100, 50, 10, 5, 1]
res = 1000-n
count = 0 
for coin in coin_types:
    q = res//coin
    count += q
    res -= coin*q

print(count)
```