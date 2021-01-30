import sys 


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

def calculate_KQ(K, Q):
    """
    K : 0~9
    Q : [NN, L]
    """
    assert len(K)==1
    assert Q[0]=="[" and Q[-1]=="]" 
    N, L = Q[1:-1].split(",")
    return f"[{int(K)*int(N)},{L}]"


string = sys.stdin.readline().strip()
stack = []
for i in string:
    stack.append(i)
    if i==")":
        store = []
        a = stack.pop()
        while True:
            a = stack.pop()
            if a =="(":
                break
            store.append(a)
        K = stack.pop()
        Q = "".join(store[::-1])
        Q = change_Q(Q)
        stack.append(calculate_KQ(K,Q))
Q = "".join(stack)
Q = change_Q(Q)
print(Q.split(",")[0][1:])