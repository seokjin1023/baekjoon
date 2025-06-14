import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
step = [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(N + 1)]
dp[1][0] = step[0]
for i in range(2, N + 1):
    dp[i][0] = max(dp[i][0], dp[i - 2][1] + step[i - 1], dp[i - 2][0] + step[i - 1])
    dp[i][1] = max(dp[i][1], dp[i - 1][0] + step[i - 1])
print(max(dp[N]))