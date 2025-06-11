import sys
from collections import deque

input = sys.stdin.readline

while True:
    s = []
    line = input().rstrip()
    if line == ".":
        break
    correct = True
    for c in line:
        if c == "(" or c == "[":
            s.append(c)
        elif c == ")":
            if len(s) == 0 or s[-1] != "(":
                correct = False
                break
            elif s[-1] == "(":
                s.pop()
        elif c == "]":
            if len(s) == 0 or s[-1] != "[":
                correct = False
                break
            elif s[-1] == "[":
                s.pop()
    if len(s) != 0:
        correct = False
    if correct:
        print("yes")
    else:
        print("no")