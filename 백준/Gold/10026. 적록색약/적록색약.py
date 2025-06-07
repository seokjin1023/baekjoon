import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N= int(input())
grid = []
for _ in range(N):
    grid.append(input())
blind_visited = [[False] * N for _ in range(N)]
non_blind_visited = [[False] * N for _ in range(N)]

directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}

def same_when_blind(front_col, back_col):
    def to_blind_color(c):
        return 'X' if c in ('R', 'G') else 'B'
    return to_blind_color(front_col) == to_blind_color(back_col)

def dfs(x, y, is_blind):
    if is_blind:
        blind_visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and same_when_blind(grid[x][y], grid[nx][ny]):
                if not blind_visited[nx][ny]:
                    dfs(nx, ny, True)
    else:
        non_blind_visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and grid[x][y] == grid[nx][ny]:
                if not non_blind_visited[nx][ny]:
                    dfs(nx, ny, False)

blind_answer = 0
non_blind_answer = 0
for i in range(N):
    for j in range(N):
        if not blind_visited[i][j]:
            dfs(i, j, True)
            blind_answer += 1
        if not non_blind_visited[i][j]:
            dfs(i, j, False)
            non_blind_answer += 1
print(str(non_blind_answer) + " " + str(blind_answer))