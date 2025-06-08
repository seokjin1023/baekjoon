import heapq
import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
edge = [[0] * n for _ in range(n)]
for _ in range(r):
    a, b, cost = map(int, input().split())
    edge[a - 1][b - 1] = cost
    edge[b - 1][a - 1] = cost

answer = 0
for i in range(n):
    visited = [False] * n
    item_num = item[i]
    que = deque()
    que.append((0, i))
    visited[i] = True
    while que:
        length, node = que.popleft()
        if not visited[node]:
            item_num += item[node]
            visited[node] = True
        for j in range(n):
            if edge[node][j] != 0 and length + edge[node][j] <= m:
                que.append((length + edge[node][j], j))
    answer = max(answer, item_num)
print(answer)

