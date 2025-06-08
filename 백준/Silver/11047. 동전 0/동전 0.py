import sys
from itertools import permutations

input = sys.stdin.readline

N, K = map(int, input().split())
value = []
for _ in range(N):
    value.append(int(input()))

answer = 0
for val in reversed(value):
    answer += K // val
    K = K % val
print(answer)