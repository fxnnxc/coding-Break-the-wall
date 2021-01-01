# 부등호

부등호에 가능한 모든 경우를 넣고, 
그 중에서 최대를 찾는 문제 최대부터 넣어서 만족하면 반환한다. 

## 방법

[9,8,7] 리스트가 있을 때, Permutation을 한다. 큰 수 부터 permutation을 하므로 해당 하는 값을 찾으면 종료하면 된다. 
987 -> 978 -> ...


```python
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


```