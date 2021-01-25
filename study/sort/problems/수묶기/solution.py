import sys 

n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for i in range(n)]
minus = [i for i in lst if i<0]
plus = [i for i in lst if i>0]


minus.sort()
plus.sort(reverse=True)

# Minus는 곱하는 게 좋다. 
summ = 0
for i in range(1, len(minus), 2):
    summ += minus[i]*minus[i-1]
if len(minus)%2==1 and 0 not in lst :
    summ += minus[-1]

for i in range(1, len(plus),2):
    summ += max(plus[i]+plus[i-1], plus[i]*plus[i-1])
        
if len(plus)%2==1:
    summ+=plus[-1]

print(summ)