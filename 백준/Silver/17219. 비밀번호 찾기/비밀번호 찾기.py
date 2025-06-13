import sys

input = sys.stdin.readline

N, M = map(int, input().split())
db = {}
for _ in range(N):
    site, pw = map(str, input().split())
    db[site] = pw
for _ in range(M):
    site = input().strip()
    print(db[site])