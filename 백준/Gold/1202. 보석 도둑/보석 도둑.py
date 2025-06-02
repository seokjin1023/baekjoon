import heapq
import bisect
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewel = []
for i in range(n):
    m, v = map(int, input().split())
    jewel.append((m, v)) #v는 최대 m은 최소로 정렬
jewel.sort()
bags = sorted(int(input()) for _ in range(k))
answer = 0
hq = []
j = 0
for bag in bags:
    #bag의 무게까지 jewel들 모두 집어넣기
    while j < n and jewel[j][0] <= bag:
        heapq.heappush(hq, -jewel[j][1])
        j += 1
    if hq:
        answer -= heapq.heappop(hq)
print(answer)


