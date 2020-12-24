import sys 

equation = sys.stdin.readline().strip()

values = equation.split("-")

total = 0
for i in values[0].split("+"):
    total += int(i)

for i in range(1, len(values)):
    sub_sum = 0
    for i in values[i].split("+"):
        sub_sum += int(i)
    total -= sub_sum

print(total)