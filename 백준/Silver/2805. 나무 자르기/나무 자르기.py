import sys
import re
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
height = sorted(list(map(int, input().split())))
low = 0
high = max(height)
answer = 0
while low <= high:
    mid = (low + high) // 2
    total = sum(h - mid for h in height if h > mid)

    if total >= M:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1
print(answer)