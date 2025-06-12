import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
value = []
for _ in range(K):
    val = int(input())
    if val == 0:
        value.pop()
    else:
        value.append(val)
print(sum(value))