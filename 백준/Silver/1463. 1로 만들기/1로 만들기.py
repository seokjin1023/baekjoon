import sys

input = sys.stdin.readline

N = int(input())
inst = [sys.maxsize] * (N + 1)
inst[1] = 0
for i in range(1, N):
    if i * 3 <= N:
        inst[i * 3] = min(inst[i * 3], inst[i] + 1)
    if i * 2 <= N:
        inst[i * 2] = min(inst[i * 2], inst[i] + 1)
    if i + 1 <= N:
        inst[i + 1] = min(inst[i + 1], inst[i] + 1)
print(inst[N])
