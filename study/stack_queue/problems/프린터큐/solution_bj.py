T = int(input())
for i in range(T):
    N,k = map(int, input().split())
    queue = input().strip().split()
    queue_sort = sorted(queue, reverse=True)
    queue = [(j,i) for i,j in enumerate(queue)]
    index = 0
    while queue:
        if queue_sort[index]==queue[0][0]:
            if queue[0][1]==k:
                print(index+1)
                break
            index +=1
        else:
            queue.append(queue[0])
        queue.pop(0)
        
        
