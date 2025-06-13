import sys

input = sys.stdin.readline

direction = {(1, 0), (-1, 0), (0, 1), (0, -1)}
def dfs(maze, visited, a, b):
    visited[a][b] = True
    for dx, dy in direction:
        nx, ny = a + dx, b + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if maze[nx][ny] == 1 and not visited[nx][ny]:
                dfs(maze, visited, nx, ny)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    maze = [[0] * N for _ in range(M)]
    for _ in range(K):
        a, b = map(int, input().split())
        maze[a][b] = 1
    visited = [[False] * N for _ in range(M)]
    answer = 0
    for i in range(M):
        for j in range(N):
            if maze[i][j] == 1 and not visited[i][j]:
                dfs(maze, visited, i, j)
                answer += 1
    print(answer)
