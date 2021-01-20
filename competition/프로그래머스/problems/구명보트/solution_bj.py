# 80 50 50 70
# Limit 100 
# 80 / 70 / 50 50
# 50 50 70 80 

def solution(people, limit):
    people.sort()
    lifeboats = 0
    left, right= 0, len(people)-1
    while left<=right:
        cumm = 0
        while True and left<=right :
            cumm+=people[right]
            if cumm>limit:
                break
            right -=1
            cumm+=people[left]
            if cumm>limit:
                break
            left +=1
        lifeboats +=1

    return lifeboats