import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
maze = []
que = deque()
for i in range(n):
    maze.append(list(map(int, input().split())))
    for j in range(m):
        if maze[i][j] == 2:
            que.append((i, j, 0))
            visited[i][j] = True
            maze[i][j] = 0
distance = {(0, 1), (0, -1), (1, 0), (-1, 0)}
while que:
    a, b, count = que.popleft()
    for dx, dy in distance:
        nx, ny = a + dx, b + dy
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            maze[nx][ny] = count + 1
            que.append((nx, ny, count + 1))
for i in range(n):
    for j in range(m):
        if not visited[i][j] and maze[i][j] == 1:
            maze[i][j] = -1
for i in range(n):
    print(*maze[i])