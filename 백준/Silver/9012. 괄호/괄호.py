import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    line = input().rstrip()
    s = []
    correct = True
    for c in line:
        if c == '(':
            s.append(c)
        else:
            if len(s) == 0:
                correct = False
                break
            else:
                s.pop()
    if len(s) != 0:
        correct = False
    if correct:
        print("YES")
    else:
        print("NO")