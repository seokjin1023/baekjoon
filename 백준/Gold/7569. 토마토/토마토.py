import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

que = deque()
for i in range(h):
    for j in range(n):
        arr[i][j] = list(map(int, input().split()))
        for k in range(m):
            if arr[i][j][k] == 1:
                que.append([i, j, k, 0])

answer = 0
directions = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
while que:
    z, x, y, day = que.popleft()
    answer = max(day, answer)
    for dx, dy, dz in directions:
        newz, newx, newy = z + dz, x + dx, y + dy
        if 0 <= newx < n and 0 <= newy < m and 0 <= newz < h:
            if arr[newz][newx][newy] == 0:
                arr[newz][newx][newy] = 1
                que.append([newz, newx, newy, day + 1])


allEnd = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                allEnd = False

if allEnd:
    print(answer)
else:
    print(-1)
