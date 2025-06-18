import sys
import heapq
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[]for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N + 1):
    graph[i] = set(graph[i])
answer = []
for i in range(1, N + 1):
    que = deque()
    visited = [False] * (N + 1)
    count = [0] * (N + 1)
    que.append((i, 0))
    visited[i] = True
    while que:
        num, go = que.popleft()
        count[num] = go
        for connect in graph[num]:
            if not visited[connect]:
                que.append((connect, go + 1))
                visited[connect] = True
    answer.append(sum(count))
print(answer.index(min(answer)) + 1)