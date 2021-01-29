- [Binary Search](#binary-search)
  - [Assigned 📌](#assigned-)
  - [Free 🤗](#free-)
  - [방법 🦄](#방법-)


# Binary Search

## Assigned 📌
[ACMIC homework Link 👨‍💻](https://www.acmicpc.net/group/practice/9719/6)
|name|solution|key words|
|:-:|:-:|:-:|
기타 레슨|[Unsolved](problems/기타레슨)|
두 용액|[Unsolved](problems/두용액)|
사냥꾼|[Solved by Bumjin](problems/사냥꾼)|
나무 자르기 |[Unsolved](problems/나무자르기)|

## Free 🤗
[Sorting👩‍💻](https://www.acmicpc.net/problemset?sort=ac_desc&algo=12)

자유롭게 풀고 풀이를 올린 문제

|name|solution|key words|info|
|:-:|:-:|:-:|:--|


## 방법 🦄

Binary Search에 대한 기본 지식입니다. 

자세한 내용은 [Basic READMD](problems/basic)를 참고하세요 

```python
# Pseudo Code
def find(v, lst):
    """
    lst에서 이분탐색으로 v의 위치를 찾아서 반환합니다. 
    lst에 존재하지 않을 경우, 값이 가장 가까운 위치를 반환합니다. 
    """
    if len(lst)==1:
        return 0
    left, right = 0, len(lst)-1
    while  right-left > 1:  # L v R : 상태까지 탐색합니다. 
        # 1. 왼쪽 또는 오른쪽에 값이 있을 경우 해당 위치 반환
        # 2. 내부에 값이 있을경우
        # 값을 찾을 경우 반환합니다. (return)
    
    #  탐색 종료 후 가능한 상태 | L v R  | v L R | L R v |
    # 3. L < v <  R 상태를 강제합니다.
    left = max(left-1, 0)
    right = min(right+1, len(lst)-1)

    # 4. v에서 가장 가까운 곳을 찾습니다.  
    values =lst[left:right+1]
    values =[(abs(t-v), i) for i, t in enumerate(values)]
    values.sort(key=lambda x:x[0])
    return values[0][1]+left
```
