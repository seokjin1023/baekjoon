import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
if K <= N:
    print(N - K)
    exit(0)
que = deque([(N, 0)])
visited = set()
answer = 100000
while que:
    location, count = que.popleft()
    if location == K:
        print(min(count, answer))
        break

    if location - 1 not in visited:
        que.append((location - 1, count + 1))
        visited.add(location - 1)
    if location + 1 not in visited:
        que.append((location + 1, count + 1))
        visited.add(location + 1)
    if location * 2 not in visited and location * 2 < K + (K - N + 1):
        que.append((location * 2, count + 1))
        visited.add(location * 2)