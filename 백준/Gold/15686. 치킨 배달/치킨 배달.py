import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city = []
chicken = []
for i in range(N):
    city.append(list(map(int, input().split())))
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i, j])


select = list(combinations(range(len(chicken)), M))
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = float('inf')

def find_distance(i, j):
    que = deque()
    visited = [[float('inf') for _ in range(N)] for _ in range(N)]
    que.append((i, j))
    visited[i][j] = 0
    while que:
        house = que.popleft()

        for dx, dy in directions:
            newx, newy = house[0] + dx, house[1] + dy
            if newx < 0 or newx >= N or newy < 0 or newy >= N:
                continue
            if visited[newx][newy] == float('inf'):
                visited[newx][newy] = visited[house[0]][house[1]] + 1
                que.append([newx, newy])
    return visited

chicken_distance = []
for i, j in chicken:
    chicken_distance.append(find_distance(i, j))
for chickenHouse in select:
    distance = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                min_distance = float('inf')
                for k in chickenHouse:
                    min_distance = min(min_distance, chicken_distance[k][i][j])
                distance += min_distance
    answer = min(answer, distance)

print(answer)


