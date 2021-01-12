n = int(input()) #피연산자 갯수
postfix = input()
nums = [0]*n
for i in range(n):
    nums[n-i-1] = int(input())
stack = []

for p in postfix:
    if 'A'<= p <= 'Z':
        stack.append(nums.pop())
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
