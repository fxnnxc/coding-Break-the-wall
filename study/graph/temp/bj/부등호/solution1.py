def check_list(lst):
    global K
    for i in range(len(lst)-1):
        if order[i]=="<" and lst[i]>lst[i+1]:
            return False 
        if order[i]==">" and lst[i]<lst[i+1]:
            return False 
    return True

def permutation(lst, values, visited):
    global K
    if len(lst)==K+1 and check_list(lst):
        return True
    if not check_list(lst):  # Speed up  초반에 틀리면 뒤에 더 붙이지 않고 종료
        return False
    for i in range(K+1):
        if not visited[i]:
            visited[i]=1
            lst.append(values[i])
            finished = permutation(lst, values, visited)
            if finished:
                return "".join([str(i) for i in lst])
            lst.pop()
            visited[i]=0

    
K = int(input())
values1 = [9-i for i in range(K+1)]
values2 = [i for i in range(K+1)]
visited1 = [0 for i in range(K+1)]
visited2 = [0 for i in range(K+1)]

order = input().strip().split()

print(permutation([], values1, visited1))
print(permutation([], values2, visited2))