import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

stack = []
num = 1
can_make = True
answer = []
for i in range(n):
    while num <= seq[i]:
        stack.append(num)
        answer.append("+")
        num += 1
    if num >= seq[i]:
        out = stack.pop()
        if out != seq[i]:
            can_make = False
            break
        else:
            answer.append("-")
if can_make:
    for c in answer:
        print(c)
else:
    print("NO")