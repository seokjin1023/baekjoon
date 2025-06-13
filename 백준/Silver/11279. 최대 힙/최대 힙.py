import sys
import heapq

input = sys.stdin.readline

N = int(input())
que = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if que:
            print(-heapq.heappop(que))
        else:
            print(0)
    else:
        heapq.heappush(que, -x)

