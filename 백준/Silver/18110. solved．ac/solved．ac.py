import sys
from collections import deque

input = sys.stdin.readline

def custom_round(n):
    return int(n + 0.5) if n > 0 else int(n - 0.5)

N = int(input())
diff = []
for _ in range(N):
    diff.append(int(input()))
diff.sort()
cut = custom_round(N * 0.15)
if N == 0:
    print(0)
else:
    print(custom_round(sum(diff[cut:len(diff) - cut]) / (N - cut * 2)))