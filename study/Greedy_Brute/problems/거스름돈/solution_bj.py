n = int(input())
coin_types = [500, 100, 50, 10, 5, 1]
res = 1000-n
count = 0 
for coin in coin_types:
    q = res//coin
    count += q
    res -= coin*q

print(count)
