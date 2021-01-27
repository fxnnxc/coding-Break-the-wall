N = int(input())#N개의 선분
lines = []
for _ in range(N):
    lines.append(list(map(int,input().split())))

pre_s, pre_e = lines[0][0],lines[0][1]
length = pre_e-pre_s

for i in range(1,N):
    cur_s,cur_e = lines[i][0],lines[i][1]
    if cur_s < pre_e: #현재_s <이전_e -> 둘이 겹치는 부분 존재
        if cur_e < pre_e:#두번째케이스 -> 아예 현재값이 이전값 안에 있는 경우
            continue
        else: #한쪽만 겹치는 경우 
            length +=  cur_e - pre_e #현재_e - 이전_e 길이 더해줌
    else: #겹치는 부분이 존재하지 않는다면
        length += cur_e - cur_s #현재선분길이만 더해줌
    pre_s,pre_e = cur_s,cur_e #현재값을 전값으로 업데이트 해줌
print(length)