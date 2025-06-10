import sys

input = sys.stdin.readline

N, K = map(int, input().split())
answer = 1
for i in range(K):
    answer *= (N - i)
for i in range(1, K + 1):
    answer //= i
print(answer)