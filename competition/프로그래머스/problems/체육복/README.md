# 체육복

https://programmers.co.kr/learn/courses/30/lessons/42862

```python
def solution(n, lost, reserve):
    reserved = [False for i in range(n+2)]
    have_uniform = [True for i in range(n+2)]
    for r in reserve:
        reserved[r] = True
    for los in lost:
        if reserved[los]==True:
            have_uniform[los] = True
            reserved[los] = False
        else:
            have_uniform[los] = False
    for r in reserve:
        if reserved[r] and not have_uniform[r-1]:
            reserved[r] = False
            have_uniform[r-1] = True
        elif reserved[r] and not have_uniform[r+1]:
            reserved[r] = False
            have_uniform[r+1] = True
    
    return sum(have_uniform[1:n+1])
```