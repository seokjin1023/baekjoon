import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
cir = deque([i + 1 for i in range(N)])
answer = []
while cir:
    for _ in range(K - 1):
        cir.append(cir.popleft())
    answer.append(cir.popleft())

print("<" + ", ".join(map(str, answer)) + ">")