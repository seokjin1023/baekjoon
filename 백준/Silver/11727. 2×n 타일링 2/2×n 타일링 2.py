import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
num = [0, 1, 3]
for i in range(3, N + 1):
    num.append((num[i - 1] + 2 * num[i - 2]) % 10007)
print(num[N])