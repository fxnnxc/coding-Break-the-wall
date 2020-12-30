import sys
input = sys.stdin.readline
listen, see = map(int, input().split())
listen_set = set()
see_set = set()

for i in range(listen):
    listen_set.add(input().strip())

for i in range(see):
    see_set.add(input().strip())

name = listen_set & see_set

print(len(name))
for i in sorted(name):
    print(i)


