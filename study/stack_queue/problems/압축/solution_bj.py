import sys 



def recurrent(lst):
    start, end = -1, -1
    for i in range(len(lst)):
        if lst[i]=="(":
            start = i
            break 
    for i in range(len(lst)-1, -1, -1):
        if lst[i]==")":
            end = i 
            break 
    if start >=0 and end >=0 and start < end:
        substring = lst[start+1:end]
        n = 0
        if start>0:
            n = int(lst[start-1])
            return lst[:start-1]+recurrent(substring)*n + lst[end+1:]
        else:
            return None
    else:
        return lst  

string = sys.stdin.readline()
print(len(recurrent(string)))
