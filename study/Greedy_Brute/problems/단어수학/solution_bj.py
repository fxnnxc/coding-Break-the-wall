N = int(input())
mapping = {}
values = []
for i in range(N):
    string = input()
    values.append(string)
    for j in range(len(string)):
        alpha = string[j]
        if alpha in mapping.keys():
            mapping[alpha] +=10**(len(string)-j) 
        else:
            mapping[alpha] = 10**(len(string)-j)

lst = list(mapping.items())
lst.sort(key=lambda x:-x[1])
mapping_values = {}
current = 9
for alpha, _ in lst:
    mapping_values[alpha] = str(current) 
    current -=1
total=0
for value in values:
    total += int("".join(list(map(lambda x:mapping_values[x], list(value)))))
print(total)