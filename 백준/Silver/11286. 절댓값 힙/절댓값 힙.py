import sys
import heapq
input = sys.stdin.readline


T = int(input())
que = []
for _ in range(T):
    x = int(input())
    if x == 0:
        if que:
            num, sign = heapq.heappop(que)
            print(-num if sign == 0 else num)
        else:
            print(0)
    else:
        if x < 0:
            heapq.heappush(que, (-x, 0))
        else:
            heapq.heappush(que, (x, 1))