import sys

input = sys.stdin.readline

def dfs(a):
    visited[a] = True
    for b in graph[a]:
        if not visited[b]:
            dfs(b)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
answer = 0
for i in range(N):
    if not visited[i]:
        dfs(i)
        answer += 1
print(answer)