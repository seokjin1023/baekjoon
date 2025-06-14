import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
answer = []
def dfs(v):
    answer.append(v)
    for vertex in graph[v]:
        if not visited[vertex]:
            visited[vertex] = True
            dfs(vertex)
visited[V] = True
dfs(V)
print(*answer)

answer.clear()
visited = [False] * (N + 1)
que = deque()
que.append(V)
visited[V] = True
while que:
    v = que.popleft()
    answer.append(v)
    for vertex in graph[v]:
        if not visited[vertex]:
            visited[vertex] = True
            que.append(vertex)
print(*answer)