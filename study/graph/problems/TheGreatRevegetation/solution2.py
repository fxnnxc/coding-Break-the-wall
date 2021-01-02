import sys 
sys.setrecursionlimit(100000)

count = 0

# S -> i, j 이면 두 edge는 연결되어 있다. N개
# graph에서 연결된 애들끼리 묶는다.  P 개 집합
def evaluate(lst, diff_graph, match):
    global N
    for i,j in diff_graph:
        if lst[match[i]]==lst[match[j]]:
            return False
    return True



def generate(lst, K, diff_graph, match):
    global count
    if len(lst)==K:
        if evaluate(lst, diff_graph, match):
            count +=1
    else:
        for i in ['A', 'B']:
            lst.append(i)
            generate(lst, K, diff_graph, match)
            lst.pop()

def solution(info):
    global N, M
    diff_info = []
    components  = [i for i in range(N)]
    for i in range(M):
        food_type, g1,g2 = info[i]
        if food_type=="S":
            small, large = min(g1, g2), max(g1, g2)
            components[large] = components[small]
        else:
            diff_info.append([components[g1], components[g2]])

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
    # print(diff_info)
    # print(sets)
    # print(match)

    generate([], len([s for s in sets if s]), diff_info, match)



N, M = map(int, input().split())
info = list(map(lambda x:(x[0], int(x[1])-1, int(x[2])-1), [sys.stdin.readline().strip().split() for i in range(M)]))
solution(info)
print(f"{count:b}", end="")