import sys 

equation = sys.stdin.readline().strip()

values = equation.split("-")
values = [list(map(int, inner_values.split("+"))) for inner_values in values]

total = sum(values[0])
for i in range(1, len(values)):
    total -= sum(values[i])

print(total)