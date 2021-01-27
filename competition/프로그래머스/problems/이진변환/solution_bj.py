def solution(s):
    answer = [0,0] 
    while s != "1":
        c = s.count("0")
        s = s.replace("0", "")
        answer[1] +=c
        s = str(bin(len(s)))[2:]
        answer[0] +=1

    return answer