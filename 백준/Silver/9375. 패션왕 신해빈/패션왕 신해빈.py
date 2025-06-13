import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, kind = input().split()
        if kind not in clothes:
            clothes[kind] = 1
        else:
            clothes[kind] += 1
    answer = 1
    for kind, count in clothes.items():
        answer *= count + 1
    answer -= 1
    print(answer)