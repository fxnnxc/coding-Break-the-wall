N, K = map(int, input().split())
lst = [str(i+1) for i in range(N)]
store = []
index = 0
for i in range(N):
    index = (index+K-1)%(N-i)
    store.append(lst.pop(index))
string = ", ".join(store)
print(f"<{string}>")