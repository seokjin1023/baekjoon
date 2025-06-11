import sys

input = sys.stdin.readline

T = int(input())
s = []
for _ in range(T):
    line = input().split()
    inst = ""
    value = 0
    if len(line) == 2:
        inst = line[0]
        value = int(line[1])
    else:
        inst = line[0]
    if inst == "push":
        s.append(value)
    elif inst == "pop":
        if len(s) != 0:
            print(s.pop(0))
        else:
            print(-1)
    elif inst == "size":
        print(len(s))
    elif inst == "empty":
        print(1 if len(s) == 0 else 0)
    elif inst == "front":
        if len(s) != 0:
            print(s[0])
        else:
            print(-1)
    elif inst == "back":
        if len(s) != 0:
            print(s[len(s) - 1])
        else:
            print(-1)