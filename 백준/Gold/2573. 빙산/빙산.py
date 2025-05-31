import sys
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

def dfs(x, y, visited, graph):
    visited[x][y] = True

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] > 0 and not visited[nx][ny]:
            dfs(nx, ny, visited, graph)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
year = 0
while True:
    visited = [[False] * M for _ in range(N)]
    found = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                visited[i][j] = True
                dfs(i, j, visited, graph)
                found = True
                break
        if found:
            break

    if not found:
        print(0)
        break
    else:
        separate = False
        for i in range(N):
            for j in range(M):
                if graph[i][j] != 0 and not visited[i][j]:
                    separate = True
                    break
            if separate:
                break
        if separate:
            print(year)
            break
    year += 1

    decrease = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                        decrease[i][j] += 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] - decrease[i][j] <= 0:
                graph[i][j] = 0
            else:
                graph[i][j] -= decrease[i][j]
