dict = {}
def out(time, words):
    if time>0 and words[time] in dict.keys():
        return True
    if time>0 and words[time-1][-1] != words[time][0]:
        return True

    dict[words[time]] = 0 
    return False

def solution(n, words):
    answer = [0,0]
    for t in range(len(words)):
        person = (t)%n
        if out(t, words):
            answer[0]=person+1
            answer[1]=(t)//n+1
            break

    return answer