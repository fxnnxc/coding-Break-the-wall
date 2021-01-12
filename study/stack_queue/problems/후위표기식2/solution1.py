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
