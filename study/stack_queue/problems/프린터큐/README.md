# 프린터 큐

## [문제](https://www.acmicpc.net/problem/1966)

우선순위 큐에서 주어진 원소가 몇번째에 출력되는지 찾는 문제이다. 

|solution|mem|time|
|:-:|:-:|:-:|
|[solution_bj.py](solution_bj.py)|28M|76ms|


## 풀이

```python
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
        


```