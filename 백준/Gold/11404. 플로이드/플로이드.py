import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())
edge = [[INF] * n for _ in range(n)]
for i in range(m):
    x, y, cost = map(int, input().split())
    edge[x - 1][y - 1] = min(cost, edge[x - 1][y - 1])
for i in range(n):
    edge[i][i] = 0
for i in range(n):
    for j in range(n):
        if i == j or edge[j][i] == INF:
            continue
        for k in range(n):
            if j == k:
                continue
            edge[j][k] = min(edge[j][k], edge[j][i] + edge[i][k])
for i in range(n):
    for j in range(n):
        if edge[i][j] != INF:
            print(edge[i][j], end=' ')
        else:
            print(0, end=' ')
    print()