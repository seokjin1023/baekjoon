import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
for i in range(1, N):
    num[i] += num[i - 1]
for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(num[j - 1])
    else:
        print(num[j - 1] - num[i - 2])