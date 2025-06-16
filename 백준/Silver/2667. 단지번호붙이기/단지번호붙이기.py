import sys
import re
from collections import deque

input = sys.stdin.readline

N = int(input())
maze = []
for _ in range(N):
    arr = [int(c) for c in input().rstrip()]
    maze.append(arr)
visited = [[False] * N for _ in range(N)]
answer = []
count = 0
direction = {(1, 0), (-1, 0), (0, 1), (0, -1)}
def dfs(i, j):
    global count
    visited[i][j] = True
    count += 1
    for dx, dy in direction:
        nx, ny = i + dx, j + dy
        if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)
for i in range(N):
    for j in range(N):
        if maze[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            answer.append(count)
            count = 0
answer.sort()
print(len(answer))
for ans in answer:
    print(ans)