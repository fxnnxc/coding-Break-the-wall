def solution(s):
    s = s[2:-2]
    lst = s.split("},{")
    lst.sort(key=lambda x:len(x))
    
    answer = []
    for i in range(len(lst)):
        temp = lst[i].split(",")
        answer.append(list(set(temp)-set(answer))[0])
    answer=list(map(int, answer))
    return answer