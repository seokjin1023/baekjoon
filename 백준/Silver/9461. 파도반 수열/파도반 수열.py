import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    length = [1, 1, 1, 2, 2]
    for i in range(5, n):
        length.append(length[i - 1] + length[i - 5])
    print(length[n - 1])