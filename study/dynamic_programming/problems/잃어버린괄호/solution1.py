
# INPUT 55-50+40

# Data Structure
# values : [55, 50, 40]
# operations : [-, +]

import re 

equation = input().strip()

values = re.sub("[+-]", " ", equation)
values = values.split()
values = list(map(int, values))
operations = re.findall("[-+]", equation)

def cal(a,b,symbol):
    if symbol=="+":
        return a+b
    elif symbol=="-":
        return a-b
    else:
        raise ValueError("Undefined Operator")

if len(values)==1:
    print(values[0])
    exit(0)

left, right = values[0] ,  values[1]
min_op = operations[0]

for i in range(1, len(operations)):
    op1, op2 = min_op, operations[i]
    C = values[i+1]

    left_candidate  = cal(left, right, op1)    # (A * B) * C
    right_candidate = cal(right, C, op2)     # A * (B * C)
    
    if cal(left_candidate, C, op2) <= cal(left, right_candidate, op1): # (A * B) * C < A * (B * C)
        left = left_candidate  
        right = C
        min_op = op2
    else:
        right = right_candidate
        min_op = op1


print(cal(left, right, min_op))