import sys 
sys.setrecursionlimit(100000)
count = 0

def evaluate(lst, diff_graph, match):
    global N
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
                return False
    return True

def generate(lst, K, diff_graph, match):
    global count
    if evaluate(lst, diff_graph, match):
        if len(lst)==K:
                count +=1
        else:
            for i in ['A', 'B']:
                lst.append(i)
                generate(lst, K, diff_graph, match)
                lst.pop()

def solution(info):
    global N, M
    diff_info = [[] for i in range(N)]
    components  = [i for i in range(N)]
    for i in range(M):
        food_type, g1,g2 = info[i]
        if food_type=="S":
            small, large = min(g1, g2), max(g1, g2)
            components[large] = components[small]
        else:
            diff_info[components[g1]].append(components[g2])
            diff_info[components[g2]].append(components[g1])

    sets = [[] for i in range(N)]
    for i in range(N):
        sets[components[i]].append(i)

    match = {i:i for i in range(N)}
    cur = -1
    for i,s in enumerate(sets):
        if len(s)==0:
            cur -=1
        cur +=1
        match[i] = cur

    generate([], len([s for s in sets if s]), diff_info, match)


N, M = map(int, input().split())
info = list(map(lambda x:(x[0], int(x[1])-1, int(x[2])-1), [sys.stdin.readline().strip().split() for i in range(M)]))
solution(info)
print(f"{count:b}", end="")