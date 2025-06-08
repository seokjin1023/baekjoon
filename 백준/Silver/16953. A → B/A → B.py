import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

answer = -1

que = deque()
que.append([a, 1])
while que:
    num, count = que.popleft()
    if num == b:
        answer = count
        break
    if num > b:
        continue

    que.append([num * 2, count + 1])
    que.append([num * 10 + 1, count + 1])
print(answer)
