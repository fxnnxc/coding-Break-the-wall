- [Binary Search Method and TestCase 🦄](#binary-search-method-and-testcase-)
  - [Binary Search Method](#binary-search-method)
  - [Test 1 : Find values which exit in the given list](#test-1--find-values-which-exit-in-the-given-list)
  - [Test 2 : Find Random Numbers](#test-2--find-random-numbers)
  - [Test 3 : TestCase using unittest](#test-3--testcase-using-unittest)
  - [Appendix](#appendix)

 
# Binary Search Method and TestCase 🦄

* Writen by Bumjin

## Binary Search Method 
```python
def find(v, lst):
    if len(lst)==1:
        return 0
    left, right = 0, len(lst)-1
    while  right-left > 1:  # 마지막 상태 : L x R : 2칸
        # 1. 왼쪽 또는 오른쪽에 값이 있을 경우
        if lst[left]==v:
            return left
        if lst[right]==v:
            return right
        # 2. 내부에 값이 있을경우
        mid = (left+right)//2
        if lst[mid] < v:
            left = mid+1
        elif lst[mid] > v:
            right = mid-1
        else:
            return mid
    # 3. L < V <  R 상태를 강제하고 가장 가까운 곳을 찾는다.  
    left = max(left-1, 0)
    right = min(right+1, len(lst)-1)
    values =lst[left:right+1]
    values =[(abs(t-v), i) for i, t in enumerate(values)]
    values.sort(key=lambda x:x[0])
    return values[0][1]+left
```

## Test 1 : Find values which exit in the given list

## Test 2 : Find Random Numbers
* If there is a given number in the list, find it
* If there is no such an element, find the closest number 
* If the given list is empty, skip the test case

## Test 3 : TestCase using unittest
* Seperate conditions
 * Length of the list : 1
 * Length of the list : 2
 * Length of the list : L>=1
* The given is already sorted increasing.


## Appendix


* Pseudo Code
```python
# Sudo Code
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

