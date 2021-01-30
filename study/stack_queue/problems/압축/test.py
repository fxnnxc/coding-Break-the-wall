
Q1 = "123[1,2]"
Q2 = "123"
Q3 = "123[1,2]123"

def change_Q(Q):
    N = 0
    start =False
    L = None
    for i in Q:
        if not start:
            N +=1
            L= i
        else:
            stack.append(i)
        if i=="[":
                start = True
                stack = []
        if i=="]":
            start = False
            count, L = "".join(stack).split(",")
            N += int(count)-1
    ret = f"[{N},{L}]"
    if Q[-1]=="]":
        ret = ret[:-1]
    return ret

print(change_Q(Q1))
print(change_Q(Q2))
print(change_Q(Q3))