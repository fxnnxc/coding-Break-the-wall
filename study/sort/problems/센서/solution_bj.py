N = int(input())
K = int(input())
lst = list(map(int, input().split()))
lst.sort()
diff = [lst[i+1]-lst[i]for i in range(len(lst)-1)]
diff.sort(reverse=True)
print(lst[-1]-lst[0]-sum(diff[:K-1]))
