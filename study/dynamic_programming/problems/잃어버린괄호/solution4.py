import sys 

equation = sys.stdin.readline().strip()

values = equation.split("-")
print(values)
#values = [list(map(int, inner_values.split("+"))) for inner_values in values]
for inner_values in values:
    print(list(map(int, inner_values.split("+"))))

total = sum(values[0])
for i in range(1, len(values)):  
    total -= sum(values[i])    

print(total)

