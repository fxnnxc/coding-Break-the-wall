N = int(input())
equation=list(input())
num_stack = []
op_stack = []
mapping = {chr(ord('A')+i):input() for i in range(N)}
for i in range(len(equation)):
    if equation[i] in mapping.keys():
        equation[i] = mapping[equation[i]]

for s in equation:
    if s in ["+", "-","*", "/"]:
        back, front = num_stack.pop(-1), num_stack.pop(-1)
        num_stack.append(str(eval(front+s+back))) 
    else:
        num_stack.append(s)

print(f"{float(num_stack[0]):.2f}")
    
