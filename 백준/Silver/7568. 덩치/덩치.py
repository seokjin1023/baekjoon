import sys

input = sys.stdin.readline

N = int(input())
w = []
for i in range(N):
    weight, tall = map(int, input().split())
    w.append([weight,tall])

rank = [0] * N
for i in range(N):
    r = 1
    for j in range(N):
        if w[i][0] < w[j][0] and w[i][1] < w[j][1]:
            r += 1
    rank[i] = r

print(*rank)