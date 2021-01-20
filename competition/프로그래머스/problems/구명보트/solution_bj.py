def solution(people, limit):
    people.sort()
    lifeboats = 0
    left, right= 0, len(people)-1
    answer = 0
    while left<=right:
        cumm = 0
        while True:
            cumm+=people[right]
            if cumm>limit:
                break
            right -=1
            cumm+=people[left]
            if cumm>limit:
                break
            left +=1
        answer +=1
        
    return answer