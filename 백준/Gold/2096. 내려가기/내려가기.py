import heapq
import bisect
import sys
input = sys.stdin.readline

n = int(input())
game = []
for _ in range(n):
    game.append(list(map(int, input().split())))

dp_max = [[0] * 3 for _ in range(2)]
dp_min = [[0] * 3 for _ in range(2)]

for i in range(n):
    cur = i % 2
    prev = (i - 1) % 2
    if i == 0:
        dp_max[cur] = game[i][:]
        dp_min[cur] = game[i][:]
    else:
        dp_max[cur][0] = max(dp_max[prev][0], dp_max[prev][1]) + game[i][0]
        dp_max[cur][1] = max(dp_max[prev][0], dp_max[prev][1], dp_max[prev][2]) + game[i][1]
        dp_max[cur][2] = max(dp_max[prev][1], dp_max[prev][2]) + game[i][2]

        dp_min[cur][0] = min(dp_min[prev][0], dp_min[prev][1]) + game[i][0]
        dp_min[cur][1] = min(dp_min[prev][0], dp_min[prev][1], dp_min[prev][2]) + game[i][1]
        dp_min[cur][2] = min(dp_min[prev][1], dp_min[prev][2]) + game[i][2]

print(max(dp_max[(n - 1) % 2]), min(dp_min[(n - 1) % 2]))