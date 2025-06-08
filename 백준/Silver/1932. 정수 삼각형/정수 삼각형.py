import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
for i in range(n):
    if i == 0:
        dp[0][0] = tri[0][0]
    else:
        dp[i][0] = dp[i - 1][0] + tri[i][0]
        for j in range(1, i):
            dp[i][j] = max(dp[i - 1][j - 1] + tri[i][j], dp[i - 1][j] + tri[i][j])
        dp[i][i] = dp[i - 1][i - 1] + tri[i][i]
print(max(dp[n - 1][:]))
