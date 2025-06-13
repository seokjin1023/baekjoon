import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
pair_num = int(input())
pair = [[] for _ in range(N + 1)]
for i in range(pair_num):
    a, b = map(int, input().split())
    pair[a].append(b)
    pair[b].append(a)
visited = [False] * (N + 1)
que = deque()
que.append(1)
visited[1] = True
answer = 0
while que:
    num = que.popleft()
    for com in pair[num]:
        if not visited[com]:
            visited[com] = True
            answer += 1
            que.append(com)
print(answer)