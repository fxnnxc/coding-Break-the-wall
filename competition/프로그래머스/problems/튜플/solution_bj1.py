def solution(s):
    s = s[2:-2]
    lst = s.split("},{")
    lst.sort(key=lambda x:len(x))
    
    answer = []
    for i in range(len(lst)):
        temp = lst[i].split(",")
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))                
    return answer