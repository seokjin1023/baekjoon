import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]
que = deque()
que.append((0, 0, 1))
visited = [[False] * M for _ in range(N)]
visited[0][0] = True
direction = {(1, 0), (-1, 0), (0, 1), (0, -1)}
while que:
    i, j, cost = que.popleft()
    for dx, dy in direction:
        nx, ny = i + dx, j + dy
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            maze[nx][ny] = cost + 1
            que.append((nx, ny, cost + 1))
print(maze[N - 1][M - 1])