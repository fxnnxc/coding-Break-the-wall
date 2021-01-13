import sys 
string = sys.stdin.readline().strip()
stack = []

for i in range(len(string)): 
    stack.append(string[i])
    if string[i]==")":
        a = stack.pop()
        store = []
        while a != "(":
            if a !=")":
                store.append(a)
            a = stack.pop()
        n = int(stack.pop())
        for _ in range(n):
            for v in store[::-1]:
                stack.append(v)


#print(stack)
print(len(stack))