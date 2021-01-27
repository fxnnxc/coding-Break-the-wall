# 키패드 누르기

https://programmers.co.kr/learn/courses/30/lessons/67256

```python
key = [[1,2,3],
      [4,5,6],
      [7,8,9],
      [-1, 0, -2]]

def find_pos(v):
    for i in range(4):
        for j in range(3):
            if key[i][j]==v:
                return [i,j]

def dist(x,y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def solution(numbers, hand):
    answer = [None]*len(numbers)
    left, right = -1, -2 
    hand = hand[0].upper()
    for idx, i in enumerate(numbers):
        if i%3==1:
            answer[idx] = 'L'
            left = i
        elif i%3==0 and i>0:
            answer[idx] = 'R'
            right = i
        else:
            left_pos = find_pos(left)
            right_pos = find_pos(right)
            key_pos = find_pos(i)
            d1, d2  = dist(left_pos, key_pos), dist(right_pos, key_pos)
            if d1 < d2:
                answer[idx] = 'L'
                left=i
            elif d1 > d2:
                answer[idx] = "R"
                right=i
            else:
                answer[idx] = hand
                if answer[idx]=="L":
                    left=i
                else:
                    right=i


    return "".join(answer)

```