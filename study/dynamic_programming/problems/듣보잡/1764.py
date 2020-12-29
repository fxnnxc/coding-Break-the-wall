import sys
input = sys.stdin.readline

listen,see = map(int,input().split())
listen_list = []
see_list = []
for i in range(listen):
    listen_list.append(input().strip())
for i in range(see):
    see_list.append(input().strip())
name = set(listen_list) & set(see_list)
name = sorted(list(name))
print(len(name))
for i in name:
    print(i)