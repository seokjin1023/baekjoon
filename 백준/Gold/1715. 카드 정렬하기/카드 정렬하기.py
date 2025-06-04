import sys
import heapq

input = sys.stdin.readline

N= int(input())
size = []
for i in range(N):
    size.append(int(input()))

heapq.heapify(size)
answer = 0
while len(size) > 1:
    card1 = heapq.heappop(size)
    card2 = heapq.heappop(size)
    answer += card1 + card2
    heapq.heappush(size, card1 + card2)
print(answer)