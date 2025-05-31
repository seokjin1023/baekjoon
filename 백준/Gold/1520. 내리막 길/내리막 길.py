import sys
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

M, N = map(int, input().split())
graph = []
for i in range(M):
    graph.append(list(map(int, input().split())))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))